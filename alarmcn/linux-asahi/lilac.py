#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    run_cmd(['sh', './get_pkg.sh', 'linux-asahi'])

def post_build():
    git_pkgbuild_commit()
