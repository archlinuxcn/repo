#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['flann']
def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith("makedepends=('cmake' 'gl2ps')"):
            line = "makedepends=('cmake' 'gl2ps' 'python2' 'libxt')"
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
