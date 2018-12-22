#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pypi_pre_build(depends=['python-quamash', 'python-fuocore'])

def post_build():
  pypi_post_build()
