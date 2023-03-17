#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Aleksana','q234rty'])

    for line in edit_file('PKGBUILD'):
        print (line.replace('xorg-xwayland-hidpi-xprop','xorg-xwayland-lily'))
