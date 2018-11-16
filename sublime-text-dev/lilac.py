# Trimmed lilac.py
#!/usr/bin/env python3
#
# This is a complex version of lilac.py for building
# a package from AUR.
#
# You can do something before/after building a package,
# including modify the 'pkgver' and 'md5sum' in PKBUILD.
#
# This is especially useful when a AUR package is
# out-of-date and you want to build a new one, or you
# want to build a package directly from sourceforge but
# using PKGBUILD from AUR.
#
# See also:
# [1] ruby-sass/lilac.py
# [2] aufs3-util-lily-git/lilac.py
# [3] octave-general/lilac.py
#

from lilaclib import *
import re

#build_prefix = 'extra-x86_64'


def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        # edit PKGBUILD
        if line.strip().startswith("depends="):
            depends = re.findall("depends=\s*\((.*)\)", line)[0]
            words = depends.split(" ")
            words.append("'desktop-file-utils'")
            line = "depends=(%s)" % (" ".join(words))
        print(line)
    for line in edit_file('sublime-text-dev.install'):
        if line.strip().startswith("cat"):
            print("update-desktop-database -q")
        print(line)

#post_build = aur_post_build

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

#if __name__ == '__main__':
#    single_main(build_prefix)
