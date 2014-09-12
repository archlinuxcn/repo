#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['python2-netlib-git']
post_build = aur_post_build

def pre_build():
  aur_pre_build()
  with fileinput.input(files=('PKGBUILD',), inplace=True) as f:
    for line in f:
      line = line.rstrip('\n')
      if line.startswith('source='):
        line = line + "\nmakedepends=('git')"
      print(line)

if __name__ == '__main__':
  single_main()
