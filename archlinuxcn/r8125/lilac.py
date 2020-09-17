#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    run_cmd(['sh', '-c', 'sed \'1,15{/ depends=/d;}\' -i PKGBUILD'])
    run_cmd(['sh', '-c', 'sed "/makedepends=/i depends=(\'linux=$(curl -s https://www.archlinux.org/packages/core/x86_64/linux/ | grep version | grep content | awk -F \'"\' \'{print $4}\')\')" -i PKGBUILD'])
