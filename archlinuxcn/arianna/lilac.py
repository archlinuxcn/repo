#!/usr/bin/python3

from lilaclib import *

def pre_build():
    update_pkgver_and_pkgrel(_G.newver)
    update_aur_repo()
