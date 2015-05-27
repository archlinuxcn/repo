#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
PATCH = b"""
--- PKGBUILD	2015-05-27 12:43:24.399140108 +0900
+++ /home/farseerfc/repo/work/cdate/PKGBUILD	2015-05-27 12:44:17.748997137 +0900
@@ -9,7 +9,7 @@
 url="http://www.vinoca.org/"
 license=('BSD')
 depends=()
-source=(http://vincasrcfiles.googlecode.com/files/$pkgname-$pkgver.tar.gz)
+source=(https://dn-vincasrcfiles.qbox.me/$pkgname-$pkgver.tar.gz)
 sha1sums=('8d799b29e9be809fb222f0e6e523a9f43a568ff4')

 build() {
@@ -17,6 +17,10 @@

   ./configure --prefix=/usr
   make || return 1
+}
+
+package() {
+  cd "$srcdir/$pkgname-$pkgver"
   make DESTDIR="$pkgdir" install || return 1
 }
"""

import subprocess

def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE)
    patch_proc.communicate(patch)

def pre_build():
    aur_pre_build()
    apply_patch("PKGBUILD", PATCH)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)


