#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Kimiblock'])
    add_depends(['qt6-quick3d'])

    for line in edit_file('PKGBUILD'):
        print (line)
        if line.startswith('function _info'):
            print ('export TERMINFO=/usr/lib/terminfo')
