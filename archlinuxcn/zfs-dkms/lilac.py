from lilaclib import *

def pre_build():
  _, newver = _G.newver.split("-")
  update_pkgver_and_pkgrel(newver)

def post_build():
  git_pkgbuild_commit()
