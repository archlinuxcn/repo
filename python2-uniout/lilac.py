# Trimmed lilac.py
#!/usr/bin/env python3

import fileinput

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  pypi_pre_build(python2=True, depends_setuptools=False)

def post_build():
  pypi_post_build()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()
