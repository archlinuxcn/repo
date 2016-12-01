#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()
  run_cmd(['wget', '-O', 'PKGBUILD', 'https://raw.githubusercontent.com/m13253/danmaku2ass/master/PKGBUILD'])

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
