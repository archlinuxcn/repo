# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  newver = _G.newver.replace('v', '')
  vers = newver.rsplit('.', 1)
  if len(vers[1]) >= 2:
    newver = vers[0] + "." + ".".join(list(vers[1]))
  else:
    newver = newver + ".REL"

  update_pkgver_and_pkgrel(newver)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()
