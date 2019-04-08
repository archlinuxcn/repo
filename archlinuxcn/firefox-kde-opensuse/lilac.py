#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'extra-x86_64'
time_limit_hours = 4

def pre_build():
    update_pkgrel()
    run_cmd(['updpkgsums'])


post_build = git_pkgbuild_commit

if __name__ == '__main__':
    single_main(build_prefix)
