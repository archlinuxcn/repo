#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    update_pkgver_and_pkgrel(_G.newver)

def post_build():
    check_library_provides()
    git_pkgbuild_commit()
    update_aur_repo()
