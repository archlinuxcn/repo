from lilaclib import *

def pre_build():
  pypi_pre_build(depends = ['python-django-jsonfield'], depends_setuptools = False)
