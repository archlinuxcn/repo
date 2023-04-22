#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['That1Calculator'])

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('build()'):
            print (line)
            print ('export CFLAGS+=w')
        else:
            print (line.replace('libdisplay-info', 'libdisplay-info-git'))
