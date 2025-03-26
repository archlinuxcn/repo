#!/usr/bin/env python3

from lilaclib import aur_pre_build
from lilaclib import edit_file


def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if 'python-bibtexparser>=2.0.0b5' in line:
            continue
        print(line)
