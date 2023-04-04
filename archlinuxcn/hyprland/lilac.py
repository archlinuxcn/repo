#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Vaxry'])
    update_pkgver_and_pkgrel(_G.newver)
