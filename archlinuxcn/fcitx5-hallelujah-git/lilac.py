from lilaclib import *

def pre_build():
  vcs_update()

def post_build():
  git_pkgbuild_commit()
  update_aur_repo()
