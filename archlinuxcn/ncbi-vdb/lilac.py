from lilaclib import *

pkgbuild_patch=b"""
diff --git a/archlinuxcn/ncbi-vdb/PKGBUILD b/archlinuxcn/ncbi-vdb/PKGBUILD
index ace2b45e14..60374b58df 100644
--- a/archlinuxcn/ncbi-vdb/PKGBUILD
+++ b/archlinuxcn/ncbi-vdb/PKGBUILD
@@ -12,15 +12,18 @@ depends=('libxml2' 'ngs' 'hdf5')
 provides=('ncbi-vdb')
 license=('custom:PublicDomain')
 options=('!strip' 'staticlibs')
-source=("https://github.com/ncbi/ncbi-vdb/archive/$pkgver.tar.gz" "$pkgname.patch")
+source=("https://github.com/ncbi/ncbi-vdb/archive/$pkgver.tar.gz" "$pkgname.patch" 
+       "issue21.patch::https://github.com/ncbi/ncbi-vdb/commit/2e0a391f952bafd387043ab292321c2e77cd5923.patch")
 sha256sums=('a6cc88e8d12f536dc96d5f60698d0ef4cf2f63e31d3d12d23da39b1de39563e1'
-            '62550416a3bd48ad8d8810a4fde593f1e6fdc6b091afbcf903842f8a43da9f58')
+            '62550416a3bd48ad8d8810a4fde593f1e6fdc6b091afbcf903842f8a43da9f58'
+            '2cbcd7da343ab1bd310846a66bf3fd10706d5b09eb143c3e316f3157be576b50')
 
 prepare(){
   cd "${pkgname}-${pkgver}"
   # ncbi build process frequently checks if we are root user which interferes 
   #   with makepkg use of fakeroot
   patch -p1 -i $srcdir/$pkgname.patch 
+  patch -p1 -i $srcdir/issue21.patch 
 }
 
 build(){
"""

def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE)
    patch_proc.communicate(patch)

def pre_build():
    aur_pre_build()
    apply_patch('PKGBUILD', pkgbuild_patch)
    run_cmd(['updpkgsums'])

def post_build():
    aur_post_build()

if __name__ == '__main__':
   single_main()
