# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

PATCH = b"""
diff --git a/archlinuxcn/vivaldi/PKGBUILD b/archlinuxcn/vivaldi/PKGBUILD
index 2b1aeb2df..9a9868e2a 100644
--- a/archlinuxcn/vivaldi/PKGBUILD
+++ b/archlinuxcn/vivaldi/PKGBUILD
@@ -4,7 +4,7 @@
 pkgname=vivaldi
 _rpmversion=2.3.1440.41-1
 pkgver=2.3.1440.41
-pkgrel=2
+pkgrel=3
 pkgdesc='An advanced browser made with the power user in mind.'
 url="https://vivaldi.com"
 options=(!strip !zipman)
@@ -48,5 +48,11 @@ package() {
         | sed -rne 's/.*(<html lang.*>.*html>).*/\1/p' \
         | w3m -I 'utf-8' -T 'text/html' \
         > "$pkgdir/usr/share/licenses/$pkgname/eula.txt"
+
+    # remove anything under /bin
+    rm -rf $pkgdir/bin
+    # move anything under /share
+    mv $pkgdir/share/* $pkgdir/usr/share/
+    rmdir $pkgdir/share
 }
"""

import subprocess

def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE)
    patch_proc.communicate(patch)

def pre_build():
    aur_pre_build()
    apply_patch("PKGBUILD", PATCH)

