#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'archlinuxcn-x86_64'
depends=['python-wtforms', 'python-wtf-peewee']

def pre_build():
  pypi_pre_build(depends=['python-flask', 'python-wtforms', 'python-peewee', 'python-wtf-peewee'])

def post_build():
  pypi_post_build()

if __name__ == '__main__':
  single_main(build_prefix)
