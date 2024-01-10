#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('yarn config set'):
            line = '#' + line
        elif line.strip().startswith('export GO111MODULE'):
            line = '#' + line
        elif line.strip().startswith('export GOPROXY'):
            line = '#' + line
        elif line.strip().startswith('depends+=(\'v2ray>=5.0.0\')'):
            line = ('#' + line + '\n'
                    "depends+=('v2ray')")
        print(line)
