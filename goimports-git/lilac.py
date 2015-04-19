#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
PATCH = b"""
--- PKGBUILD	2015-04-19 20:50:44.843350277 +0900
+++ /home/farseerfc/repo/work/goimports-git/PKGBUILD	2015-04-19 20:38:25.113344590 +0900
@@ -5,7 +5,7 @@
 pkgver=20141212
 pkgrel=1
 pkgdesc="Tool to fix (add, remove) your Go imports automatically."
-arch=("any")
+arch=("x86_64")
 url="https://github.com/bradfitz/goimports"
 license=('Other')
 makedepends=('git' 'go' 'mercurial')
@@ -21,7 +21,7 @@
 build() {
     cd "${_pkgname}"
     export GOPATH=${srcdir}
-    go get "code.google.com/p/go.tools/imports"
+    go get "golang.org/x/tools/cmd/goimports"
     go build -o "${_pkgname}"
 }
"""
post_build = aur_post_build

import subprocess

def pre_build():
    aur_pre_build()
    patch_proc = subprocess.Popen(["patch", "-p1", "PKGBUILD"], stdin=subprocess.PIPE)
    patch_proc.communicate(PATCH)

if __name__ == '__main__':
    single_main(build_prefix)



