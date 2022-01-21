#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build('linux-xanmod-edge', maintainers=['figue'])

    # pkgrel is set to ${xanmod}
    xanmod = 0
    for line in edit_file('PKGBUILD'):
        if line.startswith('xanmod='):
            xanmod = int(line.split("=")[-1])

        if line.startswith('pkgrel='):
            line = "pkgrel=" + str(xanmod)

        print(line)

    # make sure pkgrel is modified
    if xanmod == 0:
        raise ValueError('pkgrel is not set properly')
