#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

def pre_build():
  # do a pkgrel bump due to archpkg triggered rebuild
  update_pkgrel()
  aur_pre_build()

if __name__ == '__main__':
  single_main()
