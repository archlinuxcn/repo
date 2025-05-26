#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pkgver, pkgrel = get_pkgver_and_pkgrel()
  newver = _G.newver.lstrip('v')
  if newver == pkgver:
    pkgrel = str(int(pkgrel) + 1)
  else:
    pkgrel = '1'
  major, subver = newver.split('.', 1)
  for line in edit_file('PKGBUILD'):
    if line.startswith('_subver='):
      line = f'_subver="{subver}"'
    elif line.startswith('pkgrel='):
      line = f'pkgrel={pkgrel}'
    print(line)
  run_cmd(['updpkgsums'])
