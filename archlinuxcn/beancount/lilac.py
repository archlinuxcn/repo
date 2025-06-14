#!/usr/bin/python3

from lilac2.api import *

def pre_build():
  aur_pre_build(maintainers=['wzyboy'])
  for l in edit_file('PKGBUILD'):
    if l.startswith('conflicts='):
      l += '\nmakedepends=(python-setuptools)'
    print(l)

def post_build():
  aur_post_build()

