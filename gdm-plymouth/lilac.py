# Trimmed lilac.py
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

import re
from lilaclib import *


def pre_build():
  aur_pre_build()
  for line in edit_file('PKGBUILD'):
    if re.match("\s*groups=.*", line):
      continue
    print(line)

