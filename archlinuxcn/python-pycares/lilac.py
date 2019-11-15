from lilaclib import *

def pre_build():
  pypi_pre_build(
    depends=['c-ares'],
    arch=('x86_64', 'i686'),
    license = 'MIT',
  )

def post_build():
  pypi_post_build()
