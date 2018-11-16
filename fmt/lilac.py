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
    for l in edit_file('PKGBUILD'):
        if l.strip() == "..":
            l = "  -DCMAKE_INSTALL_LIBDIR=/usr/lib .."
        print(l)


#if __name__ == '__main__':
#  single_main()
