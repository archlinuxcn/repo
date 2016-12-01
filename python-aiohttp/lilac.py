#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['python-multidict-git', 'python-async_timeout', 'python-yarl']

def pre_build():
  pypi_pre_build(
    depends = ['python-chardet', 'python-multidict', 'python-async_timeout', 'python-yarl'],
    depends_setuptools = False,
    makedepends = ['cython'],
    optdepends = ['python-aiodns'],
    arch = ['i686', 'x86_64'],
  )

post_build = pypi_post_build

if __name__ == '__main__':
  single_main()
