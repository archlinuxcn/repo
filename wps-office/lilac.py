#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}]
build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if not 'PKGEXT=' in line:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
