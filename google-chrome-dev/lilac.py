#!/usr/bin/env python3

from lilaclib import *
import os

build_prefix = 'extra-x86_64'
post_build = aur_post_build
pre_build = aur_pre_build

_pkg_name = 'google-chrome-dev'

if __name__ == '__main__':
  single_main(build_prefix)

# vim: set ts=2 sw=2 et:
