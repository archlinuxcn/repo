#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build('sfnt2woff')

  for line in edit_file('PKGBUILD'):
    if line.startwith('license'):
        line = "license=('MPL' 'GPL2' 'LGPL2.1')\ndepends=('zlib')"
    print(line)


def post_build():
  aur_post_build()

if __name__ == '__main__':
  single_main()
