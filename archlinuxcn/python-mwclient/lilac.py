from lilaclib import *

def pre_build():
  pypi_pre_build(depends=['python-requests-oauthlib', 'python-six'])

def post_build():
  pypi_post_build()
