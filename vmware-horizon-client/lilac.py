#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

PATCH=b"""
diff --git a/vmware-horizon-client/PKGBUILD b/vmware-horizon-client/PKGBUILD
index 863c57b1f..6da732b33 100644
--- a/vmware-horizon-client/PKGBUILD
+++ b/vmware-horizon-client/PKGBUILD
@@ -122,7 +122,7 @@ package_vmware-horizon-client() {
 	conflicts=('vmware-view-open-client' 'vmware-view-open-client-beta' 'vmware-view-client'
 		'vmware-horizon-pcoip')
 	replaces=('vmware-horizon-pcoip')
-	depends=('gnome-icon-theme' 'gtk2' 'libpng12' 'libudev0-shim' 'libxml2' 'libxss'
+	depends=('gnome-icon-theme' 'gtk2' 'libpng12' 'libudev0-shim' 'libxml2' 'libxss' 'vmware-xkeymaps'
 		'libxtst' 'openssl' 'binutils' 'glib2' 'expat')
 	optdepends=('alsa-lib: audio support via alsa'
 		'freerdp: RDP remote desktop connections'
@@ -138,6 +138,8 @@ package_vmware-horizon-client() {
 
 	cd "${srcdir}/extract/vmware-horizon-client/"
 
+	rm -rf lib/vmware/xkeymap
+
 	mkdir -p "${pkgdir}/usr/"
 	cp -a bin/ "${pkgdir}/usr/"
 	cp -a lib/ "${pkgdir}/usr/"
"""

import subprocess

def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE)
    patch_proc.communicate(patch)

def pre_build():
    aur_pre_build()
    apply_patch("PKGBUILD", PATCH)
    update_pkgrel()

if __name__ == '__main__':
  single_main()

