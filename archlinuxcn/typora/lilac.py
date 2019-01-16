# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *


#build_prefix = 'extra-x86_64'


def pre_build():
    run_cmd(["updpkgsums"])
    aur_pre_build()

#post_build = aur_post_build

#if __name__ == '__main__':
#    single_main(build_prefix)

