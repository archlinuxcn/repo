# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

#build_prefix = 'multilib-archlinuxcn'
#pre_build = aur_pre_build
#post_build = aur_post_build

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith("makedepends"):
            line = "makedepends=('unzip' 'xorg-server-xvfb' 'xterm')"
        if line.strip().startswith("xterm"):
            line = 'xvfb-run -a -s "-extension GLX -screen 0 1280x1024x24" '+line
        print(line)
    git_add_files('PKGBUILD')
    git_commit()

#if __name__ == '__main__':
#  single_main(build_prefix)
