#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(name='linux-ck', maintainers=['graysky'])

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('_subarch'):
            print('_subarch=41') # Generic-x86-64-v3
        else:
            print(line)
