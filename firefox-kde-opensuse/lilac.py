#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}, {'archpkg': 'icu'}]
build_prefix = 'archlinuxcn-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        print(line.replace("'cargo'", ''))

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
