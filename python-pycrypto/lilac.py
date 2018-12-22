#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pypi_pre_build(arch=['i686', 'x86_64'])

def post_build():
  pypi_post_build()
