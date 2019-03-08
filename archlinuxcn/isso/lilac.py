#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    pkgver = get_pkgver_and_pkgrel()
    update_pkgver(_G.newver)
    if pkgver != _G.newver:
        update_pkgrel(1)

def post_build():
    pypi_post_build()
    update_aur_repo()
