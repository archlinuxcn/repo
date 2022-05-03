#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.endswith('CXXFLAGS=${CXXFLAGS/-g }'):
            line = (line + '\n' + '  '
                    '# -fvar-tracking-assignments is not recognized by clang' + '\n' + '  '
                    'CFLAGS=${CFLAGS/-fvar-tracking-assignments}' + '\n' + '  '
                    'CXXFLAGS=${CXXFLAGS/-fvar-tracking-assignments}')
        print(line)
