#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *


build_prefix = 'extra-x86_64'

def pre_build():
  pypi_pre_build(pypi_name='libclang-py3')

def post_build():
  pypi_post_build()

if __name__ == '__main__':
  single_main()
