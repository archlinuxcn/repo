#!/usr/bin/env python3

from lilaclib import *

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()
# vim:set ts=2 sw=2 et:

