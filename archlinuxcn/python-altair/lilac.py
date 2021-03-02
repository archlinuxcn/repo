from lilaclib import *

def pre_build():
  pypi_pre_build(
    depends = ['python-entrypoints', 'python-jinja', 'python-jsonschema', 'python-numpy', 'python-pandas', 'python-toolz'],
    depends_setuptools = False,
  )

def post_build():
  pypi_post_build()
