from lilaclib import *

def pre_build():
  vcs_update()

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()
