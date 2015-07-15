#!/usr/bin/env python3
#
# This file is for pypi package building.
#
# You don't need to edit most things except 'depends=[]'.
#
# It is too simple to say something more :)
#

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  pypi_pre_build(depends=['setuptools'])

def post_build():
  pypi_post_build()

if __name__ == '__main__':
  single_main()
