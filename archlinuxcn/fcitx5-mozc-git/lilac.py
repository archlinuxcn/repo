#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends=['fmt', 'xcb-imdkit-git', 'fcitx5-git']

update_on = [{
    'gitlab': 'fcitx/mozc'
}]

build_prefix = 'extra-x86_64'

def pre_build():
    vcs_update()
    run_cmd(['updpkgsums'])


def post_build():
    git_add_files("PKGBUILD")
    git_commit()
    update_aur_repo()

if __name__ == '__main__':
  single_main()
