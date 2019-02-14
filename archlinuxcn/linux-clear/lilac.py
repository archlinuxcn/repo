from lilaclib import *

PATCH=b"""
--- a/archlinuxcn/linux-clear/PKGBUILD
+++ b/archlinuxcn/linux-clear/PKGBUILD
@@ -115,7 +115,6 @@
     ### Setting config
         msg2 "Setting config..."
         cp -Tf $srcdir/clearlinux/config ./.config
-        make olddefconfig
 
     ### Copying i915 firmware and intel-ucode
         msg2 "Copying i915 firmware and intel-ucode..."
@@ -124,10 +123,6 @@
         cp  ${srcdir}/intel-ucode-with-caveats/06* firmware/intel-ucode/
         rm -f firmware/intel-ucode/0f*
 
-    ### Prepared version
-        make -s kernelrelease > ../version
-        msg2 "Prepared %s version %s" "$pkgbase" "$(<../version)"
-
     ### Set ACPI_REV_OVERRIDE_POSSIBLE to prevent optimus lockup
         if [ "${_rev_override}" = "y" ]; then
         msg2 "Enabling ACPI Rev Override Possible..."
@@ -153,10 +148,12 @@
         patch -Np1 -i "$srcdir/kernel_gcc_patch-$_gcc_more_v/enable_additional_cpu_optimizations_for_gcc_v8.1+_kernel_v4.13+.patch"
         fi
 
+
     ### Get kernel version
         if [ "${_enable_gcc_more_v}" = "y" ] || [ -n "${_subarch}" ]; then
         yes "$_subarch" | make oldconfig
         else
+        make olddefconfig
         make prepare
         fi
 
@@ -180,6 +177,11 @@
     ### Save configuration for later reuse
 
         cp -Tf ./.config "${startdir}/config-${pkgver}-${pkgrel}${_kernelname}"
+
+    ### Prepared version
+        make -s kernelrelease > ../version
+        msg2 "Prepared %s version %s" "$pkgbase" "$(<../version)"
+
 }
 
 build() {

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

