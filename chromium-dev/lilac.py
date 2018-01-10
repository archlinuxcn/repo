#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'archlinuxcn-x86_64'
#depends = ['openh264']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'ninja' in line and 'chrome' in line:
            print(line.replace('ninja','ninja -l$(nproc)'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
