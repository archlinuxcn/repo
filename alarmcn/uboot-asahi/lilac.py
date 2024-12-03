#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  ver, rel = _G.newver.lstrip('asahi-v').split('-')
  for line in edit_file('PKGBUILD'):
    if line.startswith('_ver='):
      line = f'_ver={ver}'
    elif line.startswith('_asahirel='):
      line = f'_asahirel={rel}'
    print(line)
  update_pkgver_and_pkgrel(pkgver)
