from lilaclib import *

def pre_build():
  pypi_pre_build(
    depends=['python-multio-provider'],
    depends_setuptools=False)

def post_build():
  git_pkgbuild_commit()
  update_aur_repo()
