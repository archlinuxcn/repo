#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['ruby-locale', 'ruby-levenshtein']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
  single_main()
