#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  pypi_pre_build()
  for l in edit_file('PKGBUILD'):
    if 'setup.py build' in l:
      l = '''\
  # Use python-setuptools installed as makedepend.
  sed -i "/distribute_setup/ s/^/#/" setup.py
''' + l
    elif l.startswith('depends='):
      l += '\nreplaces=(python3-stagger-svn)'
    print(l)

def post_build():
  pypi_post_build()

if __name__ == '__main__':
  single_main()
