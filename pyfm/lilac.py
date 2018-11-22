#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}]
build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'setup.py install' in line:
        print(line.replace('python', 'LANG=en_US.UTF-8 python'))
    elif 'mpg123' in line:
        print(line)
        print('makedepends=(\'python-setuptools\' \'python2-setuptools\')')
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
