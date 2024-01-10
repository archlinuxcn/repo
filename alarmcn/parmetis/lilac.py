#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    _newver = _G.newver.lstrip('v')
    newver = _newver.replace('-', '.')
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith("_pkgver"):
            line = f'_pkgver={_newver}'
        print(line)
    update_pkgver_and_pkgrel(newver)
