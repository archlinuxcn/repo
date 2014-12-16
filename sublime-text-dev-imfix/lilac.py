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
import os
import os.path

build_prefix = ['extra-x86_64', 'extra-i686']


def apply_linewise_patch(filename, patch):
    patch_lines = patch.split('\n')
    del_lines = list(map(lambda x: x[1:], filter(lambda x: x.startswith("-"), patch_lines)))
    add_lines = list(map(lambda x: x[1:], filter(lambda x: x.startswith("+"), patch_lines)))
    for line in edit_file(filename):
        found = False
        for d, a in zip(del_lines, add_lines):
            if line.strip() == d.strip():
                print(a)
                found = True
                break
        if not found:
            print(line)


def pre_build():
    aur_pre_build()
    # patch PKGBUILD, fixing conflict CARCH filenames
    apply_linewise_patch("PKGBUILD", r"""
-depends=('desktop-file-utils' 'libpng' 'gtk2')
+depends=('desktop-file-utils' 'libpng' 'gtk2' 'desktop-file-utils')
-        "https://raw.githubusercontent.com/Firef0x/SublimeText-zh-CN/master/dist/${CARCH}/libsublime-imfix.so"
+        "libsublime-imfix-${CARCH}.so::https://raw.githubusercontent.com/Firef0x/SublimeText-zh-CN/master/dist/${CARCH}/libsublime-imfix.so"
-        "https://raw.githubusercontent.com/Firef0x/SublimeText-zh-CN/master/dist/${CARCH}/sublime_text"
+        "sublime_text-${CARCH}::https://raw.githubusercontent.com/Firef0x/SublimeText-zh-CN/master/dist/${CARCH}/sublime_text"
-  install -Dm755 libsublime-imfix.so \
+  install -Dm755 libsublime-imfix-${CARCH}.so \
-    install -Dm755 sublime_text \
+    install -Dm755 sublime_text-${CARCH} \
""")


post_build = aur_post_build

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
    single_main(build_prefix)
