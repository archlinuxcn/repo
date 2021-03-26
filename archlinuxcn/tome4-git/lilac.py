# Trimmed lilac.py
from lilaclib import *

#build_prefix = 'extra-x86_64'

#pre_build = vcs_update

def post_build():
  git_pkgbuild_commit()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()
