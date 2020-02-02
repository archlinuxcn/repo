#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    newver = _G.newver.replace('-', '.')
    update_pkgver_and_pkgrel(newver)

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()
