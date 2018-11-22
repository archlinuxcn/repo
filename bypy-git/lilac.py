#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}, {'github':'houtianze/bypy'}]
build_prefix = 'archlinuxcn-x86_64'
depends = ['python-multiprocess']

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'python setup.py install' in line:
        print(line.replace('python', 'LANG=en_US.UTF-8 python'))
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
