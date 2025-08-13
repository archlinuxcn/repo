from lilaclib import *

def pre_build():
  pypi_pre_build(
    pep517 = True,
    makedepends = ['python-poetry-core'],
    license = "GPL-3.0-only",
  )

def post_build():
  pypi_post_build()
  update_aur_repo()
