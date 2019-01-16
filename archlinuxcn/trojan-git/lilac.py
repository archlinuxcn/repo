# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()
    vcs_update()

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()

#if __name__ == '__main__':
#    single_main(build_prefix)
