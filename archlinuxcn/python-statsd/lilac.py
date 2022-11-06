from lilaclib import *

def pre_build():
  pypi_pre_build(
    depends_setuptools = False,
    pep517 = True,
    makedepends = ['python-setuptools'],
  )

def post_build():
  git_pkgbuild_commit()
  update_aur_repo()
