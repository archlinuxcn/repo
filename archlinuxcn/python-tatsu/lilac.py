from lilaclib import pypi_pre_build, pypi_post_build

def pre_build():
  pypi_pre_build(
    makedepends = ['python-setuptools'],
    optdepends = [
      'python-colorama',
      'python-rich',
    ],
    pep517 = True,
  )

def post_build():
  pypi_post_build()
