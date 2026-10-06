import re
from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

_PATCHES = [
    'everyx-280065f977ab1032db58f35538fdd8f9d4419503.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/280065f977ab1032db58f35538fdd8f9d4419503.patch',
    'everyx-64b9e82ba888000ac3ae5d9332f4e428acfa5dff.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/64b9e82ba888000ac3ae5d9332f4e428acfa5dff.patch',
    'everyx-080024237eb63ccca982ad4c866ea93974e0d1e4.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/080024237eb63ccca982ad4c866ea93974e0d1e4.patch',
    'everyx-db10c5661143b0035a61bd198b9f130b51f9d8a5.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/db10c5661143b0035a61bd198b9f130b51f9d8a5.patch',
    'everyx-e75432c039f628b4a3085a822b5b1e5171a9b2a9.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/e75432c039f628b4a3085a822b5b1e5171a9b2a9.patch',
    'everyx-8c4cdd8b6950e0424fdf67b1542dd54002a374f5.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/8c4cdd8b6950e0424fdf67b1542dd54002a374f5.patch',
    'everyx-0ccfedb9234d744098746bce6544c8ed110419db.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/0ccfedb9234d744098746bce6544c8ed110419db.patch',
]


def pre_build():
    g.files = download_official_pkgbuild('gtk4')

    state = None
    for line in edit_file('PKGBUILD'):
        s = line.strip()

        if state == 'pkgname':
            if s == ')':
                state = None
            continue
        if state == 'skip':
            if line == '}':
                state = None
            continue
        if state == 'source':
            if s == ')':
                state = None
                for entry in _PATCHES:
                    print(f'  "{entry}"')
                print(line)
                continue
            print(line)
            continue
        if state == 'b2sums':
            if line.rstrip().endswith(')'):
                state = None
                print(line[:-1])
                for _ in _PATCHES:
                    print('        SKIP')
                print(')')
                continue
            print(line)
            continue

        if line.startswith('pkgbase='):
            continue
        if line.startswith('pkgname=('):
            print('pkgname=gtk4-everyx')
            state = 'pkgname'
            continue
        if line.startswith('pkgdesc='):
            print(line[:-1] + ", with everyx's patches\"")
            continue
        if line.startswith('arch='):
            print(line)
            print('provides+=(gtk4=$pkgver)')
            print('conflicts+=(gtk4)')
            continue
        if line.startswith('source=('):
            state = 'source'
            print(line)
            continue
        if line.startswith('b2sums=('):
            state = 'b2sums'
            print(line)
            continue
        if s == 'cd gtk':
            print(line)
            for entry in _PATCHES:
                print(f'  git apply -3 ../{entry.split("::", 1)[0]}')
            continue
        if '-D documentation=true' in line:
            print('    -D build-demos=false')
            print('    -D build-examples=false')
            print('    -D build-tests=false')
            print('    -D build-testsuite=false')
            print('    -D documentation=false')
            print('    -D introspection=enabled')
            continue
        if s.startswith('_pick demo ') or s.startswith('_pick docs '):
            continue
        if line.startswith(('package_gtk4-demos()',
                            'package_gtk4-docs()',
                            'package_gtk-update-icon-cache()')):
            state = 'skip'
            continue
        if line.startswith('package_gtk4()'):
            print('package() {')
            continue
        if s.startswith('provides=(') and not s.startswith('provides+=('):
            print(line.replace('provides=(', 'provides+=(', 1))
            continue
        print(line)

    with open('PKGBUILD') as f:
        content = f.read()
    with open('PKGBUILD', 'w') as f:
        f.write(re.sub(r'\n{3,}', '\n\n', content))


def post_build():
    git_add_files(g.files)
    git_commit()
