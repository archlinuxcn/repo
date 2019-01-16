# Trimmed lilac.py
#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  _, newver = _G.newver.split("-")
  update_pkgver_and_pkgrel(newver)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

#if __name__ == '__main__':
#  single_main()
