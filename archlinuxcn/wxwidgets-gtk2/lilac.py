#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build(maintainers=['petronny','AutoUpdateBot'])

  for line in edit_file('PKGBUILD'):
    if line.lstrip().startswith(('conflicts=', 'provides=')):
      continue
    print(line)
