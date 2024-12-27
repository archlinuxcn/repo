#!/usr/bin/env python3

from lilaclib import *
import os

build_args = ['-r', os.path.expanduser('~/chroots')]


def pre_build():
    update_pkgrel()
    vcs_update()


def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
