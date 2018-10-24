#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['depot-tools-git']

update_on = [{
    'github': 'servo/servo',
}]

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()

def pre_build():
    # run updpkgsums before and after vcs_update
    # as the PR is constantly updating to be mergable with the master branch
    run_cmd(['rm', 'pr21644.patch'])
    run_cmd(['updpkgsums'])
    vcs_update()
    run_cmd(['updpkgsums'])

if __name__ == '__main__':
    single_main(build_prefix)
