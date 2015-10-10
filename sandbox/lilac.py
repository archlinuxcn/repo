#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  # newver defaults to detected one
  update_pkgver()

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  _G = SimpleNamespace(newver='2.9')
  single_main()
