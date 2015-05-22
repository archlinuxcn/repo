#!/usr/bin/env python3

from lilaclib import *

depends = ['libfilteraudio-git',
           'tox-git']

build_prefix = 'extra-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

run_cmd(['rm', '-rf', 'qtox'])

if __name__ == '__main__':
  single_main()
