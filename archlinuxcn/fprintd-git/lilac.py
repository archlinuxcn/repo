#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

def pre_build():
    run_cmd(['updpkgsums'])
    update_pkgrel()
    vcs_update()

if __name__ == '__main__':
    single_main(build_prefix)
