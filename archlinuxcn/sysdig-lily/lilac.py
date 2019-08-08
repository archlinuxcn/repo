from lilaclib import *

def pre_build():
  update_pkgver_and_pkgrel(_G.newver.split('-')[0])

def post_build():
  git_pkgbuild_commit()
