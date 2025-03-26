#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('edk2-ovmf')

  for line in edit_file('PKGBUILD'):
    if line.strip().startswith('make -C BaseTools'):
      print("""
  export GCC_BIN="x86_64-linux-gnu-"
  export GCC_AARCH64_PREFIX=""
  export GCC_ARM_PREFIX="arm-none-eabi-"
  export GCC5_BIN="x86_64-linux-gnu-"
  export GCC5_AARCH64_PREFIX=""
  export GCC5_ARM_PREFIX="arm-none-eabi-"
""")
    elif line.strip() == 'aarch64-linux-gnu-gcc':
      line = '  x86_64-linux-gnu-gcc'
    elif line.startswith('arch='):
      line = 'arch=(aarch64) # Avoid conflicting with the official package in the x86 repo'
    print(line)
