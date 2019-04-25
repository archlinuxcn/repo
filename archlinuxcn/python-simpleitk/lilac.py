#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pypi_pre_build(arch='x86_64', pypi_name='SimpleITK')

def post_build():
  pypi_post_build()
# vim:set ts=2 sw=2 et:

