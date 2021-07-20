#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('prepare() '):
            print("sed 's/CP866/CP936/g' -i iconv-utf8+CVE-2015-1315.patch")
        else:
            print(line)
