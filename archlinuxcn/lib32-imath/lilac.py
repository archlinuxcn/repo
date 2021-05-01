#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    pkgver, pkgrel = get_pkgver_and_pkgrel()
    so_ver = pkgver[:pkgver.rfind('.')].replace('.', '_')
    add_provides([f'libImath-{so_ver}.so'])

def post_build():
    aur_post_build()
