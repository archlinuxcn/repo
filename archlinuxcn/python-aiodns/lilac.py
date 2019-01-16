# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

#build_prefix = 'extra-x86_64'
depends = ['python-pycares']

def pre_build():
  pypi_pre_build(depends=['python-pycares'], license='MIT')

def post_build():
  pypi_post_build()

#if __name__ == '__main__':
#  single_main()
