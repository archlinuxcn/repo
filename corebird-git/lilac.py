#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends = ['gtk4']
update_on = [{
    "aur": ""
},{
    "github": "baedert/corebird"
}]

build_prefix = 'archlinuxcn-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

def pre_build():
    aur_pre_build()
    for line in edit_file("PKGBUILD"):
        if line.strip().startswith("ninja"):
            line = "  ninja -C builddir -l$(nproc)"
        print(line)

if __name__ == '__main__':
  single_main()
