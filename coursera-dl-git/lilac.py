#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build(name=None, *, do_vcs_update=True):
  if os.path.exists('PKGBUILD'):
    pkgver, pkgrel = get_pkgver_and_pkgrel()
  else:
    pkgver = None

  if name is None:
    name = os.path.basename(os.getcwd())

  new_pkgver = get_pkgver_and_pkgrel()[0]
  if pkgver and pkgver == new_pkgver:
    # change pkgrel to what specified in PKGBUILD
    update_pkgrel(pkgrel)

    vcs_update()

if __name__ == '__main__':
  single_main(build_prefix)
