#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'extra-x86_64'
time_limit_hours = 4

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        print(line.replace("'cargo'", '').replace("'libvpx'", '').replace("'rust'", "'rust<=1:1.32'"))
    for line in edit_file('mozconfig'):
        if 'libvpx' in line:
            print('#' + line)
        else:
            print(line)
    run_cmd(['updpkgsums'])


post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
