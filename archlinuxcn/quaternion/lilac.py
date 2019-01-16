#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'


def pre_build():
    aur_pre_build()
    add_depends(["qt5-tools"])


post_build = aur_post_build

if __name__ == '__main__':
    single_main()
