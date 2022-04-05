#!/usr/bin/env python3

from lilaclib import *

def post_build():
    git_pkgbuild_commit()

def pre_build():
    update_pkgver_and_pkgrel(_G.newver)
