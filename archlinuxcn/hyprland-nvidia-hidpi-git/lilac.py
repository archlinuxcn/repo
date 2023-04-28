#!/usr/bin/python3

from lilaclib import *

def pre_build():
    add_depends(['libdisplay-info.so'])

    for line in edit_file('PKGBUILD'):
        print (line.replace('xorg-xwayland-hidpi-xprop', 'xorg-xwayland-lily'))

    update_pkgrel()
    vcs_update()

def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
