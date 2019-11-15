from lilaclib import *

def pre_build():
  pypi_pre_build(depends=['python-pycares'], license='MIT')

def post_build():
  pypi_post_build()
