#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['tohmais'])
    add_depends(['libdisplay-info.so'])

    for line in edit_file('PKGBUILD'):
        print (line)
        if line.strip().startswith('build()'):
            print ('export CFLAGS+=-w')
