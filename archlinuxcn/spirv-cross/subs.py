#!/usr/bin/python3

from lilaclib import *

for line in edit_file('PKGBUILD'):
    if not line.strip().startswith('ctest'):
        print(line)
