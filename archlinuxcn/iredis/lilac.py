#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    pypi_pre_build(depends = [], depends_setuptools = False)

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()

