#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('materialx')

  in_build = False
  patched = False
  for line in edit_file('PKGBUILD'):
    if line.startswith('build()'):
      in_build = True
    if in_build and not patched:
      if line.lstrip().startswith('cmake '):
        patched = True
        line = '  cmake -DNANOGUI_NATIVE_FLAGS=-march=armv8-a' + line.lstrip().lstrip('cmake')
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    print(line)

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
