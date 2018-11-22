#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}]
build_prefix = 'archlinuxcn-x86_64'
depends = ['python3-xcpf', 'python3-xcgf']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
