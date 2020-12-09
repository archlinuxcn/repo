from lilaclib import *

def pre_build():
  pypi_pre_build(
    pypi_name = 'aiosasl',
    depends_setuptools = False,
  )

def post_build():
  pypi_post_build()
