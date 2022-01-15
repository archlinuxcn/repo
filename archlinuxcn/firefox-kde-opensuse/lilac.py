#!/usr/bin/env python3
from lilaclib import *
from pyalpm import vercmp

def pre_build():
  oldver, oldrel = get_pkgver_and_pkgrel()
  aur_pre_build(maintainers=['Thaodan', 'csslayer'])
  newver, newrel = get_pkgver_and_pkgrel()
  if oldver == newver:
    update_pkgrel(rel=int(oldrel + 1))
  for line in edit_file('PKGBUILD'):
      if line.startswith('_pgo='):
          line = '_pgo=false'
      else:
          print(line)

if __name__ == '__main__':
  single_main(build_prefix)
