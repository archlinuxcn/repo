#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

import os
from lilaclib import *

build_prefix = 'extra-x86_64'

pre_build = aur_pre_build

def post_build():
    os.unlink('.pkgupdate')
    aur_post_build()

if __name__ == '__main__':
    single_main(build_prefix)

