#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  aur_pre_build()
  for l in edit_file('PKGBUILD'):
    l = l.replace("'msbuild-stable'", "'mono-msbuild'")
    print(l)
