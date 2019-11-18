#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pypi_pre_build()

def post_build():
  pypi_post_build()
  update_aur_repo()
# vim:set ts=2 sw=2 et:

