#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('validpgpkeys='):
            line = '#' + line + '\n' + "validpgpkeys=()"
        elif line.startswith('source='):
            line = '#' + line + '\n' + line + ')'
        elif line.endswith('.sig")'):
            line = '#' + line
        print(line)
    run_cmd(['updpkgsums'])
