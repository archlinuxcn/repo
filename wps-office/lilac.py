#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if not 'PKGEXT=' in line:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
