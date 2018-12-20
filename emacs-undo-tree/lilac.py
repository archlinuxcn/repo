#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith("depends"):
            line += "\nmakedepends=('git')"
        print(line)
    git_add_files('PKGBUILD')
    git_commit()

