# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *
import re

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        # edit PKGBUILD
        if line.strip().startswith("depends="):
            depends = re.findall("depends=\s*\((.*)\)", line)[0]
            words = depends.split(" ")
            words.append("'gstreamer0.10-base'")
            line = "depends=(%s)" % (" ".join(words))
        print(line)

#build_prefix = 'extra-x86_64'
#pre_build = aur_pre_build
#post_build = aur_post_build

#if __name__ == '__main__':
#  single_main()
