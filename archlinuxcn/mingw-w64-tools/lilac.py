#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['xantares'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('groups='):
            line = '\n'
        print(line)
    run_cmd(['updpkgsums'])
