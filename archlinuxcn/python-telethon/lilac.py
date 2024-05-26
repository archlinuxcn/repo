from lilaclib import *

def pre_build():
  pypi_pre_build(
    depends = ['python-pyaes', 'python-rsa'],
    depends_setuptools = False,
    license_file = 'LICENSE',
    pep517 = True,
    makedepends = ['python-setuptools'],
    optdepends = [
      'python-cryptg: alternative crypto library',
      'python-pysocks: socks proxy support',
      'python-python-socks: socks proxy support',
      'python-hachoir: parse media metadata for uploading',
      'python-pillow: resize photos for uploading',
    ]
  )

def post_build():
  pypi_post_build()
  update_aur_repo()
