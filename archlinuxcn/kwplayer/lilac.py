# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *


#build_prefix = 'extra-x86_64'

#post_build = aur_post_build

def pre_build():
    aur_pre_build()

    need_rebuild = False
    for line in edit_file('PKGBUILD'):
        # edit PKGBUILD
        if line.strip().startswith("pkgver=3.5.2"):
            need_rebuild = True
        if need_rebuild and line.strip().startswith("pkgrel=1"):
            line = "pkgrel=2"
        print(line)

#if __name__ == '__main__':
#  single_main()
