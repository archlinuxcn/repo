#!/usr/bin/python3

from lilaclib import *

def pre_build():
    _pkgver = _G.newvers[0]
    _modelver = _G.newvers[1]

    for line in edit_file('PKGBUILD'):
        if line.startswith('_pkgver='):
            line = f'_pkgver={_pkgver}'
        if line.startswith('_modelver='):
            line = f'_modelver={_modelver}'
        print(line)

    pkgver = f'{_pkgver.replace('-', '.')}_m{_modelver}'
    update_pkgver_and_pkgrel(pkgver)
