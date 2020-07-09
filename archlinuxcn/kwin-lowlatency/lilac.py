#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('groups='):
            continue
        print(line)

    vcs_update() # Avoid lilac cache for git sources
