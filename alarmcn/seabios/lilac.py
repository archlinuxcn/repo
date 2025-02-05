#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('seabios')

  in_build = False
  patched = False
  for line in edit_file('PKGBUILD'):
    if line.strip().startswith('make '):
      line = '  make CROSS_PREFIX=x86_64-linux-gnu- ' + line.lstrip()[5:]
    elif line.startswith('makedepends='):
      print('makedepends_aarch64=(x86_64-linux-gnu-gcc)')
    elif line.startswith('arch='):
      line = 'arch=(aarch64) # Avoid conflicting with the official package in the x86 repo'
    print(line)
