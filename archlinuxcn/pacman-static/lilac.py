#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

def pre_build():
  oldver, oldrel = get_pkgver_and_pkgrel()
  aur_pre_build()
  for line in edit_file('PKGBUILD'):
    if 'tm@t8m.info' in line:
        line = line[:line.find('#')] + "# Tomas Mraz <tm@t8m.info>" # sorry Tomas Mraz, your name is just corrupted UTF-8
  newver, newrel = get_pkgver_and_pkgrel()
  if oldver == newver:
    update_pkgrel(rel=int(oldrel + 1))

if __name__ == '__main__':
  single_main()
