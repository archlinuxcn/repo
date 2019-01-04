# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('sha256sums='):
            # Skip sha256sum check for the first dependency (the HTML file)
            print('sha256sums=(\'SKIP\'')
            continue
        print(line)
        if line.strip().startswith('options='):
            print('depends+=("gcc-libs")') # Should depend on gcc-libs

#post_build = aur_post_build

#if __name__ == '__main__':
#    single_main(build_prefix)

