#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

#build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()
  for line in edit_file('PKGBUILD'):
    if line.startswith('provides='):
      line = 'replaces=("google-earth")' + '\n' + line
    print(line)

#if __name__ == '__main__':
#  single_main()
