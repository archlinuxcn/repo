#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['gonX', 'jamesbt365'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('depends='):
            line = line.replace('dotnet-runtime-10.0', 'dotnet-runtime>=10.0')
        print(line)
