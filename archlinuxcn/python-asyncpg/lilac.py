from lilaclib import *

def pre_build():
  pypi_pre_build()

def post_build():
  git_pkgbuild_commit()
