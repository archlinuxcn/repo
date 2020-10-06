from lilaclib import *

def pre_build():
  pypi_pre_build(
    pypi_name = 'hstspreload',
    provides = ['python-hstspreload'],
    conflicts = ['python-hstspreload'],
    depends_setuptools = False,
  )

def post_build():
  pypi_post_build()
