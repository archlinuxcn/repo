#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['PowerBall253'])
    add_depends(['playerctl'])
    update_pkgver_and_pkgrel(_G.newver)
