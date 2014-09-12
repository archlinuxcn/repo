#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
  import os
  lilac_build(
    build_prefix = 'makepkg',
    repodir = os.path.dirname(os.path.dirname(__file__))
  )

