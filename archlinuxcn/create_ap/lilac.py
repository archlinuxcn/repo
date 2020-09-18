#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('validpgpkeys'):
            line = "validpgpkeys=('7B314BE77DBCA20E02DDBBC050BF8B712DCAD7EA') # Dct Mei <dctxmei@gmail.com>"
        print(line)
