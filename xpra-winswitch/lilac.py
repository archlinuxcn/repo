#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends = ["python2-lz4", "python-lz4", "rencode", "python2-gtkglext"]

build_prefix = 'extra-x86_64'
post_build = aur_post_build
pre_build = aur_pre_build


if __name__ == '__main__':
  single_main()
