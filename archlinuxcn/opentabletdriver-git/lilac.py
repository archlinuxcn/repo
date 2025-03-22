#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['gonX', 'jamesbt365'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('license='):
            line = "license=('LGPL-3.0-or-later')"
        elif line.startswith('makedepends='):
            line = line.replace('dotnet-sdk', 'dotnet-sdk-8.0')
        print(line)
