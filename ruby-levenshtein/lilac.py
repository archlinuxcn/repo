#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()
  for line in edit_file('PKGBUILD'):
    if line.startswith('build()'):
      line = 'package() {'
    print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
