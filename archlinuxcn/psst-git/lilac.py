#!/usr/bin/env python3



def pre_build():
    aur_pre_build(maintainers=['garionion', 'mtorromeo'])
    for line in edit_file('PKGBUILD'):

        # add cmake
        if "makedepends=" in line:
            line = "makedepends=('cargo' 'git' 'cmake')"

        # use default build
        if "--all-features" in line:
            line = line.replace("-all-features", "")

        # check breaks build
        # if "check()" in line:
        #     line = "no_check() {"

        print(line)
