#!/usr/bin/env python3

from types import SimpleNamespace
import re

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('ispc')

  for line in edit_file('PKGBUILD'):
    line = re.sub(r'\blib32-glibc\b', '', line)
    if line.startswith('checkdepends=') or line.startswith('check()'):
        line = '_' + line
    if line.lstrip().startswith('local cmake_options=('):
        line = line + " -D ISPC_INCLUDE_XE_EXAMPLES=OFF"
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    print(line)

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
