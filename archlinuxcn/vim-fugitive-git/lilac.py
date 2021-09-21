#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='xythrez')
    run_cmd(['sed', '-i', '/vim-plugins/d', 'PKGBUILD'])
    run_cmd(['sed', '-i', "s/git describe/\\0 --match 'v[0-9]*'/", 'PKGBUILD'])

def post_build():
    aur_post_build()
