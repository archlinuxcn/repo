from lilaclib import pypi_pre_build, pypi_post_build

def pre_build():
  pypi_pre_build(
    makedepends = ['python-setuptools'],
    optdepends = [
      'python-colorama',
      'python-rich',
    ],
    pep517 = True,
    conflicts = ['python-tatsu'],
    license = 'BSD-4-Clause'
  )

def post_build():
  pypi_post_build()
