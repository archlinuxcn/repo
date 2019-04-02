# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

def post_build():
    update_aur_repo()
    git_add_files("PKGBUILD")
    git_commit()

#if __name__ == '__main__':
#  single_main()
