#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pkgver, commit = _G.newver.split('@')
  pkgver = pkgver.strip()
  commit = commit.strip()
  for line in edit_file('PKGBUILD'):
    if line.startswith('_commit='):
      line = f'_commit={commit}'
    print(line)
  update_pkgver_and_pkgrel(pkgver)
