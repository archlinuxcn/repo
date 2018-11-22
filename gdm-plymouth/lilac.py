#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

import re
from lilaclib import *

build_prefix = 'archlinuxcn-x86_64'
post_build = aur_post_build

def pre_build():
  aur_pre_build()
  for line in edit_file('PKGBUILD'):
    if re.match("\s*groups=.*", line):
      continue
    print(line)

if __name__ == '__main__':
  single_main()
