#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    old_pkgver, old_pkgrel = get_pkgver_and_pkgrel()
    update_pkgrel(0)
    aur_pre_build()
    aur_pkgver, aur_pkgrel = get_pkgver_and_pkgrel()
    update_pkgver_and_pkgrel(old_pkgver, updpkgsums=False)
    update_pkgrel(old_pkgrel)
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgrel='):
            print(f'real_pkgrel={aur_pkgrel}')
        elif line.lstrip().startswith('cd $srcdir'):
            line = line.replace('${pkgrel}', '${real_pkgrel}')
        print(line)

def post_build():
    aur_post_build()
