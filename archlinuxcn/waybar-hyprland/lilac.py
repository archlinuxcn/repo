#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['PowerBall253'])
    update_pkgver_and_pkgrel()
