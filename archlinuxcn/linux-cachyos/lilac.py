#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['ptr1337','sir_lucjan'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('license='):
            line = "license=('GPL-2.0-only')"
        print(line)

    for line in edit_file('config'):
        print(line)
        if line.startswith('CONFIG_DRM_AMD_SECURE_DISPLAY'):
            print('CONFIG_AMD_PRIVATE_COLOR=y')

    run_cmd(['updpkgsums'])
