#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    oldver, oldrel = get_pkgver_and_pkgrel()
    aur_pre_build()
    newver, newrel = get_pkgver_and_pkgrel()
    if oldver == newver:
        update_pkgrel(rel=int(oldrel + 1))
    run_cmd(['sh', '-c', 'sed \'1,15{/ depends=/d;}\' -i PKGBUILD'])
    run_cmd(['sh', '-c', 'sed "/makedepends=/i depends=(\'linux=$(curl -s https://www.archlinux.org/packages/core/x86_64/linux/ | grep version | grep content | awk -F \'"\' \'{print $4}\')\')" -i PKGBUILD'])
