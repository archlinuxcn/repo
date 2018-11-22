#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}, {'github':'d-s-x/bomi'}]
build_prefix = 'archlinuxcn-x86_64'
depends = ['libchardet']

def pre_build():
    run_cmd('rm -rf bomi'.split(' '))
    aur_pre_build()

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
