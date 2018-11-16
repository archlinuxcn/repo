# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

#build_prefix = 'extra-x86_64'
PATCH = b"""
diff --git a/ipad_charge/PKGBUILD b/ipad_charge/PKGBUILD
index 6802cd1..55bc6b7 100644
--- a/ipad_charge/PKGBUILD
+++ b/ipad_charge/PKGBUILD
@@ -10,7 +10,7 @@ source=("http://www.rainbow-software.org/linux_files/${pkgname}_${pkgver}.tar.gz
 "95-ipad_charge.rules.patch"
 "ipad_charge.c.patch"
 )
-depends=('udev')
+depends=('udev' 'libusb')
 makedepends=('gcc')
 md5sums=('09b8c600efd747a36c9cc320516326cf'
          'bfc9325716cc8fcedc04f13fcf7c8693'
"""

import subprocess

def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE)
    patch_proc.communicate(patch)

def pre_build():
    aur_pre_build()
    apply_patch("PKGBUILD", PATCH)

#post_build = aur_post_build

#if __name__ == '__main__':
#  single_main(build_prefix)


