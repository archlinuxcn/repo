#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends=['ruby-coderay', 'ruby-method_source', 'ruby-slop-3']

#update_on = [{
#    'aur': 'ruby-pry'
#}]

build_prefix = 'archlinuxcn-x86_64-build'
pre_build = vcs_update

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
