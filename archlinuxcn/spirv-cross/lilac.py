#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['dbermond'])

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('ctest'):
            print(line + ' --exclude-regex spirv-cross-test-hlsl{,-opt}')
        else:
            print(line)
