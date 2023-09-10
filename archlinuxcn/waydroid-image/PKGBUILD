# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230909"
_pkgver_images_system_x86="18.1-20230909"
_pkgver_images_system_arm="18.1-20230909"
_pkgver_images_system_arm64="18.1-20230909"
_pkgver_images_vendor="18.1-20230909"
_pkgver_images_vendor_x86="18.1-20230909"
_pkgver_images_vendor_arm="18.1-20230909"
_pkgver_images_vendor_arm64="18.1-20230909"
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
sha256sums_x86_64=('f87c0b2bf5a1e4953a8bed63b3a372873c3690bfa81e05f56437713344487d51'
                   '560fd7e7a22fabe6a092b4aea1041a40bdb9ba6d967fb950ba0d8afc43d8c474')
sha256sums_i686=('68fde2e2d2a81fd53b9703b70d348b9a1ed344f7b2aa44cc689f72a284490451'
                 '90190cf102641bd7eb54d070b2e2f2a2d92ae60024bb57185bc96b0b033532ce')
sha256sums_armv7h=('0a17c0e6865a0d359312889f97033d3881ee70fa882c88d75046f3cbbcdb3fd3'
                   'd2a876acc2d6c9a82c368079950102b4ccbb35b176a8efd89de14d8273b75878')
sha256sums_aarch64=('44f02e5be89d288689298a4ba137b7e144f0ebe0bd3ef674b38a54a7920b44ca'
                    '4e6d9f35ed7b3f6a6ab676ba4f8d8a1bca32245f7748d5a6e3d338c830aa0ab7')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
