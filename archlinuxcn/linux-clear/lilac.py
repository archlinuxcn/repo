from lilaclib import *

PATCH="""
diff --git a/archlinuxcn/linux-clear/PKGBUILD b/archlinuxcn/linux-clear/PKGBUILD
index 54d613ee5..45e32e7ab 100644
--- a/archlinuxcn/linux-clear/PKGBUILD
+++ b/archlinuxcn/linux-clear/PKGBUILD
@@ -93,7 +93,8 @@ source=(
 _kernelname=${pkgbase#linux}
 : ${_kernelname:=-clear}
 
-prepare() {
+
+build() {
     cd ${_srcname}
 
     ### Add upstream patches
@@ -180,10 +181,6 @@ CONFIG_MODULE_COMPRESS_XZ=y|' ./.config
     ### Save configuration for later reuse
 
         cp -Tf ./.config "${startdir}/config-${pkgver}-${pkgrel}${_kernelname}"
-}
-
-build() {
-    cd ${_srcname}
 
     make bzImage modules
 }
"""

import subprocess
def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE)
    patch_proc.communicate(patch)   

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('_subarch='):
            print('_subarch=26')
        else:
            print(line)
    apply_patch("PKGBUILD", PATCH)
    update_pkgrel()

