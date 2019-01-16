# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  vcs_update()

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()
