# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20231028"
_pkgver_images_system_x86="18.1-20231028"
_pkgver_images_system_arm="18.1-20231028"
_pkgver_images_system_arm64="18.1-20231028"
_pkgver_images_vendor="18.1-20231028"
_pkgver_images_vendor_x86="18.1-20231028"
_pkgver_images_vendor_arm="18.1-20231028"
_pkgver_images_vendor_arm64="18.1-20231028"
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
sha256sums_x86_64=('992853ed6849fd26cb750d880016ff605910661229fb3ab22447a7e6f1c8c112'
                   'c0057b233c5dddf7b8f3bb046d3114fa34589c776743ced61840615d4d48f5bc')
sha256sums_i686=('aef8f13581b634a78cdd64dba18dc53f91e7ebf71522238f9a187ceec9b964a3'
                 '2fd1cec8add64e1b4b6d371cef2ce0ee17ba85d31214450c6eecfc8dc18ceb9f')
sha256sums_armv7h=('8884d9a3a63211e6b6e1bb73cab938817835f4b7005ea5697a684e86d915577b'
                   '6b787698ceccf15d9fe92333814d60f9183018c6f0bbc1c0d8b6688978f97734')
sha256sums_aarch64=('406adff7e346eab019a51287e49765a6d6c24d62c0a47eb74eb8ea9ad2c384ee'
                    'e67f0d92907bd74083f1f83da701609c94c4cdbd8ba7c662c27d3e94194aac70')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
