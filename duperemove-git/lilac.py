#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
PATCH = b"""
diff --git a/duperemove-git/PKGBUILD b/duperemove-git/PKGBUILD
index a9bb749..db423d3 100644
--- a/duperemove-git/PKGBUILD
+++ b/duperemove-git/PKGBUILD
@@ -8,6 +8,7 @@ arch=('any')
 url="https://github.com/markfasheh/duperemove"
 license=('GPL')
 makedepends=('git')
+depends=('sqlite')
 source=("$pkgname"::'git://github.com/markfasheh/duperemove.git#branch=master')
 md5sums=( 'SKIP' )
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



