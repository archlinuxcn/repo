#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
  vcs_update()

if __name__ == '__main__':
  single_main()
