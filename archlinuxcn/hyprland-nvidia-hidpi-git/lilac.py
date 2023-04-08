#!/usr/bin/python3

from lilaclib import *

def pre_build():
    update_pkgrel()
    vcs_update()

    for line in edit_file('PKGBUILD'):
        line = line.replace('libdisplay-info', 'libdisplay-info-git')
        line = line.replace('xorg-xwayland-hidpi-xprop', 'xorg-xwayland-lily')
        print (line)

def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
