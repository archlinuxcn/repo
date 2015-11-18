#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  pypi_pre_build(
    depends = ['python-chardet'],
    depends_setuptools = False,
    makedepends = ['cython'],
    arch = ['i686', 'x86_64'],
  )

post_build = pypi_post_build

if __name__ == '__main__':
  single_main()
