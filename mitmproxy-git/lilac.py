#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
  aur_pre_build()
  for line in edit_file('PKGBUILD'):
    if line.startswith('source='):
      line = line + "\nmakedepends=('git')"
    print(line)

if __name__ == '__main__':
  single_main()
