#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

_pkgname = 'racerd'
pkgname = _pkgname + '-git'

def pre_build():
  aur_pre_build(pkgname)

  for line in edit_file('PKGBUILD'):
    if line.startswith('arch='):
        line += "\nprovides=('" + _pkgname + "')"
        line += "\nconflicts=('" + _pkgname + "')"
    print(line)


if __name__ == '__main__':
  single_main(build_prefix)

# vim:set ts=2 sw=2 et:
