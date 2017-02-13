#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'bogus-nxdomain.china.conf' in line:
        print(line)
        print(line.replace('bogus-nxdomain.china.conf','google.china.conf'))
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
