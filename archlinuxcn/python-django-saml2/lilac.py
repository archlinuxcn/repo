from lilaclib import *

def pre_build():
  pypi_pre_build(pypi_name = 'djangosaml2',
                 depends = ['python-django', 'python-defusedxml', 'python-pysaml2'],
                 depends_setuptools = False)
