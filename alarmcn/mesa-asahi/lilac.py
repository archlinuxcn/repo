#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  asahiver = _G.newver.lstrip('asahi-')
  for line in edit_file('PKGBUILD'):
    if line.startswith('_asahiver='):
      line = f'_asahiver={asahiver}'
    print(line)
  run_cmd(['updpkgsums'])
