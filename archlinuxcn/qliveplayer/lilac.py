#!/usr/bin/env python3
from lilaclib import *


def pre_build():
    update_pkgver_and_pkgrel(_G.newver.lstrip('v').lstrip())

def post_build():
    git_commit()
    update_aur_repo()

if __name__ == '__main__':
    single_main()
