# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['S13ntist'])
    for line in edit_file('PKGBUILD'):
        if "git describe --long --tags" in line:
            line = '    printf "%s.%s" "$(git describe --tags --long | cut -d- -f1)" "$(git rev-list --count HEAD)"'

        # use nodejs
        if line.startswith("depends="):
            line = 'depends=("nodejs")'
        print(line)

#if __name__ == '__main__':
#  single_main()
