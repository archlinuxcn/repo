# Trimmed lilac.py
#!/usr/bin/env python3

import fileinput

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  update_pkgver_and_pkgrel(_G.newver)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

#if __name__ == '__main__':
#  single_main()
