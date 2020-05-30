#!/usr/bin/env python3
from lilaclib import *


def pre_build():
    update_pkgver_and_pkgrel(_G.newver.lstrip('v').lstrip())

def post_build():
    git_add_files('PKGBUILD')
    git_add_files('0001-use-system-font-and-use-stylename.patch')
    git_commit()

if __name__ == '__main__':
    single_main()
