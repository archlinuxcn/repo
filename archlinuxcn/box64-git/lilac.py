#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['mogwai'])

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('git describe --long --tags'):
            print("git describe --long --tags | sed 's/\\([^-]*-g\\)/r\\1/;s/-/./g;s/v//'")
        else:
            print(line)
