# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *


#build_prefix = 'archlinuxcn-x86_64'

#pre_build = vcs_update

def post_build():
    git_add_files("PKGBUILD")
    git_commit()

#if __name__ == '__main__':
#    single_main(build_prefix)

