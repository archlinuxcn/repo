from lilaclib import *

def pre_build():
  pypi_pre_build(depends = ['python-lxml', 'python-six', 'python-requests'], depends_setuptools = False)
