#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'extra-x86_64'
time_limit_hours = 4

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('_pgo'):
            print('_pgo=')
        else:
            print(line.replace("'cargo'", '').replace("'libvpx'", ''))
    for line in edit_file('mozconfig'):
        if not line.startswith('#') and ('libvpx' in line or 'enable-rust-simd' in line):
            print('#' + line)
        else:
            print(line)
    run_cmd(['echo', '"ac_add_options --disable-elf-hack"', '>>mozconfig'])
    run_cmd(['updpkgsums'])


post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
