#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build('ttf2eot')

  for line in edit_file('PKGBUILD'):
    if line.startwith('depends'):
      line = "depends=('gcc-libs')"
    print(line)


def post_build():
  aur_post_build()

if __name__ == '__main__':
  single_main()
