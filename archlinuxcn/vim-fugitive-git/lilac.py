#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='xythrez')
    run_cmd(['sed', '-i', '/vim-plugins/d', 'PKGBUILD'])

def post_build():
    aur_post_build()
