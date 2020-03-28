from lilaclib import *

def pre_build():
  pypi_pre_build(depends = ['python-django-appconf'], depends_setuptools = False)
