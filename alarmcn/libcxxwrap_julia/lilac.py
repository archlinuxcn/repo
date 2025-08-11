#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pkgver, _ = _G.newver.split('@')
  pkgver = pkgver.split('+')[0]
  update_pkgver_and_pkgrel(pkgver.strip())
