#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  pypi_pre_build(pypi_name='Wand')

  for l in edit_file('PKGBUILD'):
    if l.lstrip().startswith('python3 setup.py install'):
      l += '\nrm $pkgdir/usr/README.rst'
    print(l)

def post_build():
  pypi_post_build()

if __name__ == '__main__':
  single_main()

# vim:set ts=2 sw=2 et:
