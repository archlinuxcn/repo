from lilaclib import *

def pre_build():
  pypi_pre_build(
    depends = ['python-typing_extensions'],
    depends_setuptools = False,
    license = 'Apache-2.0',
    pep517 = False,
    makedepends = ['python-setuptools'],
  )

def post_build():
  pypi_post_build()

