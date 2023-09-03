# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230902"
_pkgver_images_system_x86="18.1-20230902"
_pkgver_images_system_arm="18.1-20230902"
_pkgver_images_system_arm64="18.1-20230902"
_pkgver_images_vendor="18.1-20230902"
_pkgver_images_vendor_x86="18.1-20230902"
_pkgver_images_vendor_arm="18.1-20230902"
_pkgver_images_vendor_arm64="18.1-20230902"
pkgname=waydroid-image
pkgver="${_pkgver_images_system//-/_}"
pkgrel=1
pkgdesc="LineageOS-based Android images for Waydroid"
arch=(x86_64 i686 armv7h aarch64)
url='https://waydro.id'
license=(Apache)
optdepends=(waydroid)
_srcprefix="https://sourceforge.net/projects/waydroid/files/images"
source_x86_64=("$_srcprefix/system/lineage/waydroid_x86_64/lineage-$_pkgver_images_system-VANILLA-waydroid_x86_64-system.zip"
               "$_srcprefix/vendor/waydroid_x86_64/lineage-$_pkgver_images_vendor-MAINLINE-waydroid_x86_64-vendor.zip")
source_i686=("$_srcprefix/system/lineage/waydroid_x86/lineage-$_pkgver_images_system_x86-VANILLA-waydroid_x86-system.zip"
             "$_srcprefix/vendor/waydroid_x86/lineage-$_pkgver_images_vendor_x86-MAINLINE-waydroid_x86-vendor.zip")
source_armv7h=("$_srcprefix/system/lineage/waydroid_arm/lineage-$_pkgver_images_system_arm-VANILLA-waydroid_arm-system.zip"
               "$_srcprefix/vendor/waydroid_arm/lineage-$_pkgver_images_vendor_arm-MAINLINE-waydroid_arm-vendor.zip")
source_aarch64=("$_srcprefix/system/lineage/waydroid_arm64/lineage-$_pkgver_images_system_arm64-VANILLA-waydroid_arm64-system.zip"
                "$_srcprefix/vendor/waydroid_arm64/lineage-$_pkgver_images_vendor_arm64-MAINLINE-waydroid_arm64-vendor.zip")
sha256sums_x86_64=('6877cf870ecd7c1552015c2b88a1efc9fab55e570cb0695dd8f1a5a7f6d2110e'
                   'a0e79cc5b347ef14bf333f3c72e0e5a9603140f4bdf2d46836c05dcdb338520c')
sha256sums_i686=('3d41de6e4f9c533939cea82bdf75e0a8ad9a5c9bc21c36f6e8af76c002c1a00b'
                 '36ac154ef7b0063e069a2559dbf10141a9eb0a300c589a50055ea4223dad8c74')
sha256sums_armv7h=('3a847966018d88cab6b0c9004bd54f6b84b0d1fcd7d3ef0797a7b4a0992c015a'
                   '09f72b00c63725593c84f883329a44adbb407ccb44d40c7d590ae683aed0a54d')
sha256sums_aarch64=('1f922bb3ff68a8c3ce0363cfe29a60170d08123c791e09edd4a62dad29d9efc1'
                    '91070a4a5c3748c6665e0b7ab9e76bb79c5d8660f41131ac59f8c3caad7d7702')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
