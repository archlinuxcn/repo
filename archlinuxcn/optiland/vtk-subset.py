#!/usr/bin/python
"""Make optiland import only the VTK modules it uses.

Arch's `vtk.py` imports every VTK module, which needs most of vtk's
optdepends (and a different set on each architecture). This scans the given
source directories for `vtk.<name>` uses, writes a shim module importing just
the VTK modules providing those names, and rewrites `import vtk` to use it.

Usage: vtk-subset.py HIERARCHY_DIR SHIM_FILE SHIM_MODULE SRCDIR...

Fails if any VTK use can't be handled, so that new usage in a future
release breaks the build rather than the installed package.
"""

import ast
import glob
import os
import re
import sys

# Modules that only register object factory overrides (rendering backend,
# interactor styles, text rendering, platform render windows/interactors).
# They're never referenced by name, but are needed for rendering to work.
FACTORY_MODULES = ('vtkInteractionStyle', 'vtkRenderingFreeType',
                   'vtkRenderingOpenGL2', 'vtkRenderingUI')

IMPORT_RE = re.compile(r'^([ \t]*)import vtk(?=[ \t#]|$)', re.M)
FROM_UTIL_RE = re.compile(r'^([ \t]*)from vtk\.util(?=[. \t])', re.M)


def load_hierarchy(hdir):
    owner = {}
    for path in glob.glob(os.path.join(hdir, '*-hierarchy.txt')):
        with open(path) as f:
            for line in f:
                fields = [x.strip() for x in line.split(';')]
                if len(fields) >= 3:
                    name = re.split(r'\s*[:=]\s*', fields[0])[0]
                    owner.setdefault(name, fields[2])
    if not owner:
        sys.exit(f'no VTK hierarchy files found in {hdir}')
    # Python-only helpers (mutable, reference, ...) and constants aren't in
    # the hierarchy files; they live in vtkCommonCore.
    import vtkmodules.vtkCommonCore as core
    for name in dir(core):
        if not name.startswith('_'):
            owner.setdefault(name, 'vtkCommonCore')
    return owner


def vtk_imports(tree):
    """Yield (lineno, description) of every import of the `vtk` module."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == 'vtk' or alias.name.startswith('vtk.'):
                    yield node.lineno, f'import {alias.name}' + (
                        f' as {alias.asname}' if alias.asname else '')
        elif isinstance(node, ast.ImportFrom) and node.level == 0:
            mod = node.module or ''
            if mod == 'vtk' or mod.startswith('vtk.'):
                yield node.lineno, f'from {mod} import ...'
        elif isinstance(node, ast.Call) and node.args:
            # Dynamic imports, e.g. importlib.import_module("vtk")
            func = node.func
            fname = func.attr if isinstance(func, ast.Attribute) else getattr(func, 'id', '')
            arg = node.args[0]
            if (fname in ('import_module', '__import__') and
                    isinstance(arg, ast.Constant) and isinstance(arg.value, str) and
                    (arg.value == 'vtk' or arg.value.startswith('vtk.'))):
                yield node.lineno, f'{fname}({arg.value!r})'


def main():
    hdir, shim_file, shim_module, *srcdirs = sys.argv[1:]
    owner = load_hierarchy(hdir)

    names = set()
    errors = []
    rewritten = []
    for srcdir in srcdirs:
        for path in sorted(glob.glob(os.path.join(srcdir, '**', '*.py'),
                                     recursive=True)):
            with open(path, encoding='utf-8') as f:
                text = f.read()
            tree = ast.parse(text, path)
            imports = list(vtk_imports(tree))
            for lineno, desc in imports:
                if desc not in ('import vtk', 'from vtk.util.numpy_support import ...'):
                    errors.append(f'{path}:{lineno}: unsupported `{desc}`')
            uses = [node for node in ast.walk(tree)
                    if isinstance(node, ast.Attribute) and
                    isinstance(node.value, ast.Name) and node.value.id == 'vtk']
            if uses and not any(d == 'import vtk' for _, d in imports):
                errors.append(f'{path}: uses `vtk.` without `import vtk`')
            for node in uses:
                if node.attr == 'util':
                    continue
                if node.attr not in owner:
                    errors.append(f'{path}:{node.lineno}: unknown `vtk.{node.attr}`')
                names.add(node.attr)
            if not imports:
                continue

            new = IMPORT_RE.sub(rf'\1import {shim_module} as vtk', text)
            new = FROM_UTIL_RE.sub(r'\1from vtkmodules.util', new)
            left = list(vtk_imports(ast.parse(new, path)))
            if left:
                errors += [f'{path}:{n}: `{d}` not rewritten' for n, d in left]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new)
            rewritten.append(path)

    if errors:
        sys.exit('\n'.join(errors))

    bymod = {}
    for name in sorted(names):
        bymod.setdefault(owner[name], []).append(name)
    lines = ['"""VTK subset used by optiland (generated at package build time)."""',
             '', '# ruff: noqa', '']
    lines += [f'import vtkmodules.{m}' for m in FACTORY_MODULES]
    lines += ['import vtkmodules.util.numpy_support',
              'from vtkmodules import util', '']
    for mod, mod_names in sorted(bymod.items()):
        lines.append(f'from vtkmodules.{mod} import (')
        lines += [f'    {n},' for n in mod_names]
        lines.append(')')
    lines += ['', '__all__ = ['] + [f'    {n!r},' for n in sorted(names)] + [']', '']
    with open(shim_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f'{shim_module}: {len(names)} names from {len(bymod)} modules; '
          f'rewrote {len(rewritten)} files', file=sys.stderr)


if __name__ == '__main__':
    main()
