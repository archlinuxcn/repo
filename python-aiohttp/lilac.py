#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['python-async_timeout', 'python-yarl']

def pre_build():
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgver='):
      line = 'pkgver=%s' % g.oldver
    print(line)

  run_cmd(['updpkgsums'])

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
