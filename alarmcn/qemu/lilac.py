#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('qemu-base')

  for line in edit_file('PKGBUILD'):
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    print(line)
