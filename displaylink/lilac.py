#!/usr/bin/python3

from lilaclib import *

build_prefix = 'archlinuxcn-x86_64'

depends = ['evdi']

pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main()
