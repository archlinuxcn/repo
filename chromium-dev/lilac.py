#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}]
build_prefix = 'archlinuxcn-x86_64'
depends = ['gn-git']
time_limit_hours = 4

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'ninja' in line and 'chrome' in line:
            print(line.replace('ninja','ninja -l$(nproc)'))
        elif 'makedepends=(' in line:
            print(line.replace('makedepends=(', 'makedepends=("libva" '))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
