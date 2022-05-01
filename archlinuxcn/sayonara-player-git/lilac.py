#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    for line in edit_file('PKGBUILD'):
        if "DWITH_TESTS" in line:
            line = ''

        if "make test" in line:
            line = ''

        print(line)
