#!/usr/bin/env python3

import re
from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('conflicts='):
            line = 'conflicts=(nvidia-dkms)'
        else:
            line = line.replace('nvidia.conf', 'nvidia-dkms.conf')
        print(line)

def post_build():
    aur_post_build()
