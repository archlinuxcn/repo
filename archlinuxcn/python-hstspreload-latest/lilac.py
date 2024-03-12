from lilaclib import *

def pre_build():
  pypi_pre_build(
    pypi_name = 'hstspreload',
    provides = ['python-hstspreload'],
    conflicts = ['python-hstspreload'],
    depends_setuptools = False,
    license = 'BSD-3-Clause',
  )

def post_build():
  pypi_post_build()
