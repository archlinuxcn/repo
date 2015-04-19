#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
PATCH = b"""
diff --git a/lsw/PKGBUILD b/lsw/PKGBUILD
index 728c100..2ed092b 100644
--- a/lsw/PKGBUILD
+++ b/lsw/PKGBUILD
@@ -1,9 +1,10 @@
+# Maintainer: Jiachen Yang <farseerfc@gmail.com>
 # Contributor: Evan Gates      <evan.gates@gmail.com>
 #              Dag  Odenhall   <dag.odenhall@gmail.com>
 #              Raphael Nestler
 pkgname=lsw
-pkgver=0.2
-pkgrel=2
+pkgver=0.3
+pkgrel=1
 pkgdesc="List window names"
 license=(MIT)
 arch=(i686 x86_64)
@@ -11,7 +12,8 @@ url="http://tools.suckless.org/lsw"
 depends=(libx11)
 source=("http://dl.suckless.org/tools/$pkgname-$pkgver.tar.gz"
         "makefile.patch")
-md5sums=('5ddd61d04ff084a39494b2aa06c00b65'
+
+md5sums=('3ae42c41a7ceda8ddf6e0fbab0866f79'
          'ae850a6a044a11f01a73f56c2f1c5520')

 build() {
@@ -20,6 +22,10 @@ build() {

 	patch "$srcdir/$pkgname-$pkgver/Makefile" "$srcdir/makefile.patch"
 	make X11INC=/usr/lib/X11 X11LIB=/usr/lib/X11
+}
+
+package(){
+	cd -- "$srcdir/$pkgname-$pkgver"
 	make PREFIX=/usr MANPREFIX=/usr/share/man DESTDIR="$pkgdir" install

 	install -m644 -D LICENSE "$pkgdir/usr/share/licenses/$pkgname/COPYING"
"""
post_build = aur_post_build

import subprocess

def pre_build():
    aur_pre_build()
    patch_proc = subprocess.Popen(["patch", "-p1", "PKGBUILD"], stdin=subprocess.PIPE)
    patch_proc.communicate(PATCH)

if __name__ == '__main__':
    single_main(build_prefix)


