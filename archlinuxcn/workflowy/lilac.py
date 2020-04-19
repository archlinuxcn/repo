#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    version = _G.newver.lstrip('v')
    update_pkgver_and_pkgrel(version)
    run_cmd(['updpkgsums'])
    version = version.replace('-','_')
    update_pkgver_and_pkgrel(version)

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
