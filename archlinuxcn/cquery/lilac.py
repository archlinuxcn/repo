# Trimmed lilac.py
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *


def pre_build():
  update_pkgver_and_pkgrel(_G.newver)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()

