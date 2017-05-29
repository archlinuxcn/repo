#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['python-multidict-git', 'python-async_timeout', 'python-yarl']

def pre_build():
  old_pkgver, pkgrel = get_pkgver_and_pkgrel()
  pkgver = _G.newver.lstrip('v')

  if old_pkgver == pkgver:
    update_pkgrel(pkgrel)
  else:
    update_pkgver(pkgver)
    update_pkgrel(1)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
