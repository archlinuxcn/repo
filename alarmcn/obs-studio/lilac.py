#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('obs-studio')

  for line in edit_file('PKGBUILD'):
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    if line.lstrip().startswith('-DCMAKE_INSTALL_PREFIX'):
      print('    -DENABLE_QSV11=OFF \\')
    print(line)

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
