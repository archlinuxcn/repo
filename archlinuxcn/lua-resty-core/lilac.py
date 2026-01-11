from lilaclib import *

def pre_build():
  newver = _G.newver.replace('R', '.r')
  update_pkgver_and_pkgrel(newver)

def post_build():
  git_pkgbuild_commit()
