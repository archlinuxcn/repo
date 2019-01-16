from lilaclib import *

def pre_build():
  version = _G.newver.replace('-', '')
  update_pkgver_and_pkgrel(version)

def post_build():
  git_pkgbuild_commit()
