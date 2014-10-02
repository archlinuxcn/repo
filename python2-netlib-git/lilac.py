#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
  aur_pre_build()
  for line in edit_file('PKGBUILD'):
    if line.startswith('makedepends=('):
      line = line.replace(')', " 'python2-setuptools')")
    print(line)

if __name__ == '__main__':
  single_main()
