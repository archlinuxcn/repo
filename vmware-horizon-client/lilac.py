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
index 6da4e8fc4..cde7c812f 100644
--- a/vmware-horizon-client/PKGBUILD
+++ b/vmware-horizon-client/PKGBUILD
@@ -16,7 +16,7 @@ pkgname=('vmware-horizon-client'
 pkgver=4.9.0
 _build=9507999
 _cart='CART19FQ3'
-pkgrel=3
+pkgrel=6
 pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop'
 arch=('x86_64')
 url='https://www.vmware.com/go/viewclients'
@@ -122,7 +122,7 @@ package_vmware-horizon-client() {
 	conflicts=('vmware-view-open-client' 'vmware-view-open-client-beta' 'vmware-view-client'
 		'vmware-horizon-pcoip')
 	replaces=('vmware-horizon-pcoip')
-	depends=('gnome-icon-theme' 'gtk2' 'libpng12' 'libudev0-shim' 'libxml2' 'libxss'
+	depends=('gnome-icon-theme' 'gtk2' 'libpng12' 'libudev0-shim' 'libxml2' 'libxss' 'vmware-xkeymaps'
 		'libxtst' 'openssl' 'binutils' 'glib2' 'expat')
 	optdepends=('alsa-lib: audio support via alsa'
 		'freerdp: RDP remote desktop connections'
@@ -137,6 +137,7 @@ package_vmware-horizon-client() {
 	install=vmware-horizon-client.install
 
 	cd "${srcdir}/extract/vmware-horizon-client/"
+	rm -rf lib/vmware/xkeymap
 
 	mkdir -p "${pkgdir}/usr/"
 	cp -a bin/ "${pkgdir}/usr/"
@@ -148,6 +149,7 @@ package_vmware-horizon-client() {
 	cp -a debug/ "${pkgdir}/usr/share/doc/vmware-horizon-client/"
 
 	cd "${srcdir}/extract/vmware-horizon-pcoip/"
+	rm -rf pcoip/lib/vmware/xkeymap
 
 	mkdir -p "${pkgdir}/usr/"
 	cp -a pcoip/lib/ "${pkgdir}/usr/"
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

