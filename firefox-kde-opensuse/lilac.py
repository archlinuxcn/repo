#!/usr/bin/env python3

from lilaclib import *

import os
import re
import ntpath

build_prefix = 'archlinuxcn-x86_64'

def get_source_list():
    buf = ''
    for line in open("PKGBUILD"):
        if not line.strip().startswith("#"):
            buf += line

    match = re.search('source=\(([^)]+)\)', buf)
    result = match.group(1)

    return [ntpath.basename(f) for f in result.split()]

def pre_build():
    # clean the patches
    l = get_source_list()
    for f in l:
        if os.path.exists(f):
            os.remove(f)

    aur_pre_build()

def post_build():
    aur_post_build()

if __name__ == '__main__':
  single_main()
