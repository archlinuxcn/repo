
from lilaclib import *

import subprocess

def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE, text=True)
    patch_proc.communicate(patch)

def pre_build():
    aur_pre_build()
    add_makedepends(['git'])
    apply_patch('PKGBUILD', PATCH)

PATCH=r"""
diff --git a/archlinuxcn/marktext-git/PKGBUILD b/archlinuxcn/marktext-git/PKGBUILD
index b10901150f..ef1933f0f6 100644
--- a/archlinuxcn/marktext-git/PKGBUILD
+++ b/archlinuxcn/marktext-git/PKGBUILD
@@ -13,7 +13,7 @@ pkgdesc='A simple and elegant open-source markdown editor that focused on speed
 arch=(x86_64)
 url='https://marktext.app'
 license=(MIT)
-_electron=electron11
+_electron=electron17
 depends=("$_electron"
          libxkbfile
          libsecret
@@ -42,7 +42,7 @@ pkgver() {
 }
 
 prepare() {
-    local _electronDist=$(dirname $(realpath $(which $_electron)))
+    local _electronDist=$(pacman -Qql $_electron | grep -E "/usr/lib/electron[[:digit:]]*/$")
     local _electronVersion=$($_electron --version | sed -e 's/^v//')
     cd "$pkgname"
     jq 'del(.devDependencies["electron"], .scripts["preinstall", "postinstall"])' \
@@ -58,6 +58,7 @@ prepare() {
 
 build() {
     cd "$pkgname"
+    export GYP_DEFINES="openssl_fips="
     yarn --cache-folder "$srcdir/node_modules" run \
         electron-rebuild
     node .electron-vue/build.js
@@ -70,7 +71,7 @@ package() {
     install -Dm755 "$_pkgname.sh" "$pkgdir/usr/bin/$_pkgname"
     local _dist=build/linux-unpacked/resources
     install -Dm644 -t "$pkgdir/usr/lib/$_pkgname/" "$_dist/app.asar"
-    cp -a "$_dist"/{app.asar.unpacked,hunspell_dictionaries} "$pkgdir/usr/lib/$_pkgname/"
+    cp -a "$_dist"/app.asar.unpacked "$pkgdir/usr/lib/$_pkgname/"
     local _rg_path="$pkgdir/usr/lib/marktext/app.asar.unpacked/node_modules/vscode-ripgrep/bin/"
     mkdir -p $_rg_path
     ln -sf /usr/bin/rg "$_rg_path"
"""

