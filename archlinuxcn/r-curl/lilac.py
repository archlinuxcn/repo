#!/usr/bin/env python3

from lilaclib import *


def pre_build():
  for line in edit_file('PKGBUILD'):
    if line.startswith('_pkgver='):
      line = f'_pkgver={_G.newver}'
      print(line)

def post_build():
  git_pkgbuild_commit()
# vim:set ts=2 sw=2 et:

