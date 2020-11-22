#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    pkgver, pkgrel = get_pkgver_and_pkgrel()
    so_ver = pkgver[:pkgver.rfind('.')].replace('.', '_')
    add_provides([f'libHalf-{so_ver}.so', f'libIex-{so_ver}.so', f'libIexMath-{so_ver}.so', f'libIlmImf-{so_ver}.so', f'libIlmImfUtil-{so_ver}.so', f'libIlmThread-{so_ver}.so', f'libImath-{so_ver}.so'])

def post_build():
    aur_post_build()
