#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['ruby-yard', 'ruby-maruku']

def pre_build():
  aur_pre_build()

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
