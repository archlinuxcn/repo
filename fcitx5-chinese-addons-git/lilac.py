#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends=['fmt', 'xcb-imdkit-git', 'fcitx5-git', 'libime-git', ('fcitx5-qt-git', 'fcitx5-qt5-git')]

build_prefix = 'extra-x86_64'

pre_build = vcs_pre_build

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()

if __name__ == '__main__':
  single_main()
