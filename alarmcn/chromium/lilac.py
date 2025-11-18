#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

import shutil

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('chromium')

  for line in edit_file('PKGBUILD'):
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    print(line)

  run_protected(["updpkgsums"])

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
