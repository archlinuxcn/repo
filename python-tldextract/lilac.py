#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  pypi_pre_build(
    pypi_name='tldextract',
    depends=['python-idna', 'python-requests-file'],
  )

  for l in edit_file('PKGBUILD'):
    if 'setup.py install' in l:
      l += '''

  _pyver=$(python -c 'import sysconfig; print(sysconfig.get_python_version())')
  # use the snapshot version, because generating a new one requires Internat access and root permission
  ln -s .tld_set_snapshot "$pkgdir/usr/lib/python$_pyver/site-packages/tldextract/.tld_set"
'''
    print(l)

def post_build():
  pypi_post_build()
  update_aur_repo()

if __name__ == '__main__':
  single_main()
