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
    run_cmd(["rm", "-f",  "master-pdf-editor-4.0.60_qt5.amd64.tar.gz"])
    aur_pre_build()


#if __name__ == '__main__':
#  single_main(build_prefix)
