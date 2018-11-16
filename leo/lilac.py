# Trimmed lilac.py
#!/usr/bin/env python3
#
# Auto update if have upstream new ver. but pkgver drop 'v'
# eg: pkgver v0.1 => 0.1
#

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  update_pkgver_and_pkgrel(_G.newver)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

#if __name__ == '__main__':
#  single_main()
