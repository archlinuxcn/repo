# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

#build_prefix = 'archlinuxcn-x86_64'

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('replaces='):
            continue
        if line.startswith('JIT='):
            line = 'JIT="YES"'
        if line.startswith('AOT='):
            line = 'AOT="YES"'
        print(line)


#post_build = aur_post_build

#if __name__ == '__main__':
#  single_main()
