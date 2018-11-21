#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#


from lilaclib import *

#build_prefix = 'extra-x86_64'
#pre_build = aur_pre_build
#post_build = aur_post_build

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if "java-environment>=" in line:
            line = line.replace("java-environment>=7","jdk8-openjdk")
            print(line)


if __name__ == '__main__':
  single_main()

