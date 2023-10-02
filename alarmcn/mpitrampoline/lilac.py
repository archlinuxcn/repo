#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pkgver = _G.newver.lstrip('v')
  _mpiconstants_ver = _G.newvers[1].lstrip('v')
  _mpiwrapper_ver = _G.newvers[2].lstrip('v')
  for line in edit_file('PKGBUILD'):
    if line.startswith('_mpiconstants_ver='):
      line = f'_mpiconstants_ver={_mpiconstants_ver}'
    if line.startswith('_mpiwrapper_ver='):
      line = f'_mpiwrapper_ver={_mpiwrapper_ver}'
    print(line)
  update_pkgver_and_pkgrel(pkgver)
