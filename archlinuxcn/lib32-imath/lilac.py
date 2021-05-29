#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='rodrigo21')
    pkgver, pkgrel = get_pkgver_and_pkgrel()
    so_ver = pkgver[:pkgver.rfind('.')].replace('.', '_')
    add_provides([f'libImath-{so_ver}.so'])

def post_build():
    check_library_provides()
    aur_post_build()
