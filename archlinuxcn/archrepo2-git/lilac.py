from lilaclib import *

def pre_build():
  update_pkgrel()
  vcs_update()

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
