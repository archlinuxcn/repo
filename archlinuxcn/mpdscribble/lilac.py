# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

#build_prefix = 'extra-x86_64'
#pre_build = aur_pre_build
#post_build = aur_post_build

def pre_build():
    aur_pre_build(maintainers=['jasonwryan'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('makedepends'):
            line = "makedepends=('boost' 'systemd' 'meson' 'ninja')"
        print(line)
#if __name__ == '__main__':
#  single_main()
