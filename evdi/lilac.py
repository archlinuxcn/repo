#!/usr/bin/python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('makedepends'):
            if line.find('linux-headers') == -1:
                index = line.rfind(')')
                right = line[index:]
                line = line[:index] + ', linux-headers' + right
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
        single_main()

