#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    flag = True
    for line in edit_file('PKGBUILD'):
        print(line)
        if line.strip().startswith('OPTS=') and flag:
            flag = False
            print('OPTS+=" QMAKE_CFLAGS_RELEASE=-w QMAKE_CXXFLAGS_RELEASE=-w"')
