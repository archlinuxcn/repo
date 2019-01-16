#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()
  for l in edit_file('PKGBUILD'):
    if l.startswith('pkgrel'):
      l += '\nepoch=1'
    print(l)

if __name__ == '__main__':
  single_main(build_prefix)
