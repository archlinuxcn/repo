#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends=['fmt', 'xcb-imdkit-git', 'fcitx5-git', 'libime-git', ('fcitx5-qt-git', 'fcitx5-qt5-git')]

build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()
    add_depends(['fcitx5-qt5-git'])

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
