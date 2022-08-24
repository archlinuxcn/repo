#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['interfiber'])
    add_replaces(['font-victor-mono'])

def post_build():
  git_add_files("PKGBUILD")
  git_commit()
