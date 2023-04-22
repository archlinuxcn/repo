#!/usr/bin/python3

from lilaclib import *

def pre_build():
    update_pkgrel()
    vcs_update()

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('build()'):
            print (line)
            print ('export CFLAGS+=-w')
        else:
            print (line.replace('xorg-xwayland-hidpi-xprop', 'xorg-xwayland-lily'))

def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
