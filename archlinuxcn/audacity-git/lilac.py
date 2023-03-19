#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['ongyx'])

    for line in edit_file('PKGBUILD'):
        print (line.replace('pro-audio', 'pro-audio-git'))
