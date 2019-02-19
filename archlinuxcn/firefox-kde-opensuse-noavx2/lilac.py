#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}, {'archpkg': 'icu'}]
build_prefix = 'extra-x86_64'
depends = ['kmozillahelper']
time_limit_hours = 4

PATCH=b"""
--- firefox-kde-opensuse/PKGBUILD	2019-02-16 22:01:34.550313014 +0900
+++ firefox-kde-opensuse-noavx2/PKGBUILD	2019-02-19 01:39:33.236385507 +0900
@@ -6,7 +6,7 @@
 #_lowmem=true
 
 # build with PGO
-_pgo=true
+_pgo=
 
 # globalmenu
 # to support globalmenu a patch from ubuntu is applied
@@ -15,7 +15,7 @@
 # /view/head:/debian/patches/unity-menubar.patch
 
 _pkgname=firefox
-pkgname=$_pkgname-kde-opensuse
+pkgname=$_pkgname-kde-opensuse-noavx2
 pkgver=65.0.1
 pkgrel=1
 pkgdesc="Standalone web browser from mozilla.org with OpenSUSE patch, integrate better with KDE"
@@ -119,8 +119,8 @@
     patch -Np1 -i "$srcdir"/pgo_fix_missing_kdejs.patch
 
     echo "ac_add_options --enable-lto" >> .mozconfig
-    echo "ac_add_options --disable-elf-hack" >> .mozconfig
   fi
+  echo "ac_add_options --disable-elf-hack" >> .mozconfig
 }
 
 build() {
"""


import subprocess

def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE)
    patch_proc.communicate(patch)

def pre_build():
    aur_pre_build("firefox-kde-opensuse")
    apply_patch("PKGBUILD", PATCH)

    for line in edit_file('PKGBUILD'):
        print(line.replace("'cargo'", ''))

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)


