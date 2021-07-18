#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  aur_pre_build(maintainers='iyanmv')
  for line in edit_file('PKGBUILD'):
    if line.startswith('provides='):
      line = 'replaces=("google-earth")' + '\n' + line
    print(line)

