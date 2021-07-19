#!/usr/bin/env python3

from lilaclib import *


def pre_build():
    aur_pre_build()
    pkgver = ""
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('_pkgver='):
            pkgver = line[len('_pkgver='):].strip().replace('-', '.')
        elif line.strip().startswith('pkgver='):
            print(f'pkgver={pkgver}')
        else:
            print(line)

if __name__== '__main__':
    single_main('extra-x86_64')
