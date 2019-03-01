from lilaclib import *

def pre_build():
  add_depends(["ruby-thread_safe"])
  update_pkgver_and_pkgrel(_G.newver)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

