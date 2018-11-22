#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#


from lilaclib import *

# build_prefix = 'extra-x86_64'
# pre_build = aur_pre_build
# post_build = aur_post_build

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main()


