#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build('sonixd', maintainers=['j.r', 'zxp19821005'])
    for line in edit_file('PKGBUILD'):
        # fix gendesk, source use --name which generate default file name PKGBUILD.desktop
        # should use --pkgname
        if 'gendesk -q -f -n' in line:
            line = 'gendesk -q -f -n --categories="Development" --pkgname="${pkgname}" --exec="${pkgname} %U"'
        print(line)
