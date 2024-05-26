# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20240413"
_pkgver_images_system_x86="18.1-20240413"
_pkgver_images_system_arm="18.1-20240413"
_pkgver_images_system_arm64="18.1-20240413"
_pkgver_images_vendor="18.1-20240413"
_pkgver_images_vendor_x86="18.1-20240413"
_pkgver_images_vendor_arm="18.1-20240413"
_pkgver_images_vendor_arm64="18.1-20240413"
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
sha256sums_x86_64=('c13a30422411cee641884c9cc3f64edad097afd530e7f2d2f2c6bf7e4980a636'
                   'cf77494e1b72f3031bf9b04e789eec3915a21a27197d1e48a01dfc8932ea9962')
sha256sums_i686=('3143a9aba7b5ed7696e200b0fffbeaf92dfc5c95b8c00ebc6856f16c9ec3b7e1'
                 '7dfd068f2de7e7c34a1bde6405c437b3d44f2b3fe42e95ea24314b4943423c03')
sha256sums_armv7h=('762f91d2c89a788b1eec90bd32e6cd54f43aa53d1a6e3169e380bc36524381d5'
                   'a0159ee65d5e6f96e595a59db0e806860abd80fcb02de3379ad8d131ca968f6a')
sha256sums_aarch64=('818b2b80d74e899de676b8bc75fb504f2a0f1998e876693bdaa32746eefb1b8b'
                    '0af5a6741b6a079cf21790196793fe305d260b94f6f7c4467de7cb89cbbf4152')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
