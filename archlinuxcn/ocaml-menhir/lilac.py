#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  aur_pre_build(maintainers=['soimort', 'xuanruiqi'])
  for line in edit_file('PKGBUILD'):
    if line.startswith('arch='):
      line = 'arch=(armv7h aarch64 x86_64)'
    print(line)
