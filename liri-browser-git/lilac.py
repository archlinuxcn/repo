#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['qml-material-git', 'libvlc-qt-git']

post_build = aur_post_build

def pre_build():
    run_cmd(["git", "clean", "-x", "-d", "-f", "."])
    aur_pre_build()

if __name__ == '__main__':
    single_main(build_prefix)


