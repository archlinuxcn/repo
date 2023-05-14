#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['ImperatorStorm'])

    for line in edit_file('PKGBUILD'):
        if not line.strip().startswith('depends=(python-argparse'):
            print (line)
