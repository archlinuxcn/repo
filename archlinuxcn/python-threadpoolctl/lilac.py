#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pypi_pre_build(license='BSD', license_file='LICENSE')

def post_build():
  pypi_post_build()
  update_aur_repo()
# vim:set ts=2 sw=2 et:

