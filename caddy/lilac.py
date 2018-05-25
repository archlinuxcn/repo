#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'

def insert(path, i):
    env_list = list("    export CGO_ENABLED=0\n")
    with open('PKGBUILD', 'r') as file:
        content = file.readlines()
        content[i:] = env_list + content[i:]

    with open('PKGBUILD', 'w') as file:
        file.writelines(content)

def pre_build():
    path = 'PKGBUILD'
    env = list("export CGO_ENABLED=0\n")
    for i, line in enumerate(edit_file(path)):
        if line.startwith('prepare()'):
            insert(path, i+1)
    
post_build = aur_post_build

if __name__ == '__main__':
  single_main()
