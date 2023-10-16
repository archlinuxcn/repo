#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['memchr'])
    add_makedepends(['jq'])

    for line in edit_file('PKGBUILD'):
        print(line)
        if line.strip().startswith('cd Hyprland'):
            print('git config pull.rebase true')
            print('pick_mr 3571')
