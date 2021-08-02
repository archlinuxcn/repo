#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    newver = _G.newver.lstrip('v')
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('_pkgver='):
            print(f'_pkgver={newver}')
        elif line.strip().startswith('pkgver='):
            print(f'pkgver={newver.replace("-", "")}')
        else:
            print(line)


def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
