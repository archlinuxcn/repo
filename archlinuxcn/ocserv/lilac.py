# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
    update_pkgver_and_pkgrel(_G.newver)

def post_build():
    git_pkgbuild_commit()

#if __name__ == '__main__':
#    single_main(build_prefix)

