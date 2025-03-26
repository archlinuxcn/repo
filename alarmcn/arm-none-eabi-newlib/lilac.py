#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('arm-none-eabi-newlib')

  for line in edit_file('PKGBUILD'):
    # This is an (any) package but we need to set it to arch-specific
    # so that it won't be copied to the x86 repo...
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    print(line)
