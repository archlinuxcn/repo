#!/usr/bin/env python3

from lilaclib import *


def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('depot-tools-auth') or line.strip().startswith('roll-dep-svn'):
            pass # delete this line
        else:
            print(line)


if __name__ == '__main__':
  single_main()
