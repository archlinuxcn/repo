#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
update_on = [{'aur':'enpass-bin'}]

pre_build = aur_pre_build
post_build = aur_post_build

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line == "install='enpass-bin.install'":
            line = ""
        print(line)

def post_build():
    aur_post_build()

    git_add_files(['PKGBUILD'])
    git_commit()

if __name__ == '__main__':
    single_main()
