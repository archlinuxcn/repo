#!/usr/bin/python3

from lilaclib import *

def pre_build():
    substrings = _G.newver.split('-Release.')
    for line in edit_file('PKGBUILD'):
        if line.startswith('_commit_hash='):
            line = f'_commit_hash={substrings[1]}'
        print(line)

    update_pkgver_and_pkgrel(substrings[0])
