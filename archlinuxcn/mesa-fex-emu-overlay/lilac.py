import os
import re
import shlex
import subprocess
import tempfile

from lilaclib import *

# Must match the order of the archpkg entries in lilac.yaml:
# (official pkgbase, prefix of the generated PKGBUILD variables)
_SOURCES = [
    ('mesa', '_mesa'),
    ('lib32-mesa', '_lib32_mesa'),
]

_VERSUFFIX = re.compile(r'[<>=].*$')


def _uniq(items, skip):
    '''Dedupe keeping the order of first appearance and drop the ones whose
    name (without version constraint) is in skip.'''
    seen = set(skip)
    res = []
    for item in items:
        name = _VERSUFFIX.sub('', item)
        if name not in seen:
            seen.add(name)
            res.append(item)
    return res


def _official_srcinfo(pkgbase):
    '''Fetch the official PKGBUILD with lilac's own helper into a scratch
    directory and parse `makepkg --printsrcinfo` output into
    (epoch, "pkgver-pkgrel", [pkgname...], [provides...], [depends...]).'''
    cwd = os.getcwd()
    with tempfile.TemporaryDirectory(prefix=f'{pkgbase}-official-') as d:
        os.chdir(d)
        try:
            download_official_pkgbuild(pkgbase)
            srcinfo = subprocess.check_output(
                ['makepkg', '--printsrcinfo'], text=True)
        finally:
            os.chdir(cwd)

    info = {}
    pkgnames = []
    provides = []
    depends = []
    for line in srcinfo.splitlines():
        line = line.strip()
        if ' = ' not in line:
            continue
        key, value = line.split(' = ', 1)
        if key == 'pkgname':
            pkgnames.append(value)
        elif key == 'provides':
            provides.append(_VERSUFFIX.sub('', value))
        elif key == 'depends' or key.startswith('depends_'):
            depends.append(value)
        elif key in ('pkgver', 'pkgrel', 'epoch') and key not in info:
            info[key] = value

    # drop names that are real packages
    return (info.get('epoch', ''), f"{info['pkgver']}-{info['pkgrel']}",
            pkgnames, _uniq(provides, pkgnames), depends)


def pre_build():
    generated = {}
    replaced = set()
    all_depends = []
    for (pkgbase, prefix), ver in zip(_SOURCES, _G.newvers):
        # nvchecker's archpkg source reports "pkgver-pkgrel" (no epoch)
        if not ver:
            raise Exception(f'no version for {pkgbase} from nvchecker')
        epoch, pkgbuild_ver, pkgnames, provides, depends = \
            _official_srcinfo(pkgbase)
        if pkgbuild_ver != ver:
            # the split list would not correspond to the version we are
            # about to download; let lilac retry on its next run
            raise Exception(
                f'official {pkgbase} PKGBUILD is {pkgbuild_ver}, '
                f'nvchecker says {ver}')
        generated[f'{prefix}_ver'] = f'{epoch}:{ver}' if epoch else ver
        generated[f'{prefix}_pkgs'] = '(' + ' '.join(pkgnames) + ')'
        generated[f'{prefix}_provides'] = '(' + ' '.join(provides) + ')'
        replaced.update(pkgnames, provides)
        all_depends.append((prefix, depends))

    # Runtime dependencies of the drivers for mesa-fex-dummy to pull into the
    # rootfs. Drop the ones on mesa itself, which the dummy replaces
    # (e.g. vulkan-* -> vulkan-mesa-implicit-layers, lib32-mesa -> mesa).
    for prefix, depends in all_depends:
        depends = _uniq(depends, replaced)
        generated[f'{prefix}_depends'] = \
            '(' + ' '.join(shlex.quote(d) for d in depends) + ')'

    for line in edit_file('PKGBUILD'):
        name = line.split('=', 1)[0]
        if name in generated:
            line = f'{name}={generated[name]}'
        print(line)

    # pkgver follows x86_64 mesa (pkgver part of "pkgver-pkgrel"); a
    # lib32-mesa-only change or a manual rebuild keeps pkgver and bumps pkgrel.
    # Also runs updpkgsums.
    update_pkgver_and_pkgrel(_G.newvers[0].rsplit('-', 1)[0])
