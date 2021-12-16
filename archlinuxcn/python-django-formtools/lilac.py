from lilaclib import *

def pre_build():
  pypi_pre_build(depends = ['python-django', 'python-setuptools-scm'], depends_setuptools = False)
