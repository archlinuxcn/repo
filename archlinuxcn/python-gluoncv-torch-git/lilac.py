#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  update_pkgrel()
  update_pkgver_and_pkgrel("0.0.3."+_G.newver)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()
# vim:set ts=2 sw=2 et:

