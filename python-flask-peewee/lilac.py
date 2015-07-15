#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

pre_build = vcs_update
depends = ['python-flask', 'python-wtforms', 'python-peewee', 'python-wtf-peewee']

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
