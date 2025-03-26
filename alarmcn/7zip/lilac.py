#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('7zip')

  for line in edit_file('PKGBUILD'):
    # Do not replace for now since the build server package db isn't updated yet
    if line.startswith('replaces='):
      line = '_' + line
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    print(line)

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
