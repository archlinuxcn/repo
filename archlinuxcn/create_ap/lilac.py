#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('validpgpkeys'):
            line = "validpgpkeys=()"
        elif line.startswith('source'):
            line = line + ')'
        elif line.startswith('sig'):
            line = '#' + line
        print(line)
    run_cmd(['updpkgsums'])
