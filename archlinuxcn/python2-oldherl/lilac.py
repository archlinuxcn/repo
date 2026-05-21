#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  aur_pre_build(maintainers=['micwoj92','andreas_baumann'])

  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=python2-oldherl'
    if line.startswith('pkgdesc='):
      line = 'pkgdesc="python2 for oldherl packaging only. Do not use"\nprovides=python2'
    print(line)

def post_build():
  aur_post_build()
