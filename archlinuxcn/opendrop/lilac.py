# Trimmed lilac.py
from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  update_pkgver_and_pkgrel(_G.newver.lstrip('v'))
  run_cmd(['updpkgsums'])

#if __name__ == '__main__':
#  single_main()
