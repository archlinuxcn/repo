#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgver'):
      print('pkgver=%s' % _G.newver)
      continue
    print(line)

  run_cmd(['updpkgsums'])

def post_build():
  git_add_files(['PKGBUILD'])
  git_commit()


if __name__ == '__main__':
  single_main()
