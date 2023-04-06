#!/usr/bin/python3

def pre_build():
  aur_pre_build()
  for l in edit_file('PKGBUILD'):
    if l.startswith('conflicts='):
      l += '\nmakedepends=(python-setuptools)'
    print(l)

def post_build():
  aur_post_build()

