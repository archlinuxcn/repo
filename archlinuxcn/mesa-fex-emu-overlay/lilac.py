import os
import re
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


def _official_srcinfo(pkgbase):
    '''Fetch the official PKGBUILD with lilac's own helper into a scratch
    directory and parse `makepkg --printsrcinfo` output into
    (epoch, "pkgver-pkgrel", [pkgname...], [provides...]).'''
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
    for line in srcinfo.splitlines():
        line = line.strip()
        if ' = ' not in line:
            continue
        key, value = line.split(' = ', 1)
        if key == 'pkgname':
            pkgnames.append(value)
        elif key == 'provides':
            provides.append(_VERSUFFIX.sub('', value))
        elif key in ('pkgver', 'pkgrel', 'epoch') and key not in info:
            info[key] = value

    # keep order of first appearance, drop names that are real packages
    seen = set(pkgnames)
    uniq = []
    for p in provides:
        if p not in seen:
            seen.add(p)
            uniq.append(p)

    return (info.get('epoch', ''), f"{info['pkgver']}-{info['pkgrel']}",
            pkgnames, uniq)


def pre_build():
    generated = {}
    for (pkgbase, prefix), ver in zip(_SOURCES, _G.newvers):
        # nvchecker's archpkg source reports "pkgver-pkgrel" (no epoch)
        if not ver:
            raise Exception(f'no version for {pkgbase} from nvchecker')
        epoch, pkgbuild_ver, pkgnames, provides = _official_srcinfo(pkgbase)
        if pkgbuild_ver != ver:
            # the split list would not correspond to the version we are
            # about to download; let lilac retry on its next run
            raise Exception(
                f'official {pkgbase} PKGBUILD is {pkgbuild_ver}, '
                f'nvchecker says {ver}')
        generated[f'{prefix}_ver'] = f'{epoch}:{ver}' if epoch else ver
        generated[f'{prefix}_pkgs'] = '(' + ' '.join(pkgnames) + ')'
        generated[f'{prefix}_provides'] = '(' + ' '.join(provides) + ')'

    for line in edit_file('PKGBUILD'):
        name = line.split('=', 1)[0]
        if name in generated:
            line = f'{name}={generated[name]}'
        print(line)

    # pkgver follows x86_64 mesa (pkgver part of "pkgver-pkgrel"); a
    # lib32-mesa-only change or a manual rebuild keeps pkgver and bumps pkgrel.
    # Also runs updpkgsums.
    update_pkgver_and_pkgrel(_G.newvers[0].rsplit('-', 1)[0])
