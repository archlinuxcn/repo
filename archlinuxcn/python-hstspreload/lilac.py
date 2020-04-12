from lilaclib import *

def pre_build():
  pypi_pre_build(
    depends_setuptools = False,
  )

def post_build():
  pypi_post_build()
  update_aur_repo()
