#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('embree')

  for line in edit_file('PKGBUILD'):
    line = line.replace('AVX512SKX', 'NEON2X')
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    print(line)

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
