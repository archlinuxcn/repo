#!/usr/bin/env python3
from lilaclib import *

#build_prefix = 'archlinuxcn-x86_64'
#pre_build = aur_pre_build
#post_build = aur_post_build

def pre_build():
    run_cmd(["rm", "-rf", "go-for-it-git"])
    aur_pre_build(maintainers=['btd1337'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('makedepends'):
            line = "makedepends=('vala' 'git' 'cmake' 'intltool')"
        print(line)

#if __name__ == '__main__':
#  single_main()
