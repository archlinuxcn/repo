# Maintainer: enamulhasanabid <enamulhabid at gmail dot com>
# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20240914"
_pkgver_images_system_x86="18.1-20240914"
_pkgver_images_system_arm="18.1-20240914"
_pkgver_images_system_arm64="18.1-20240914"
_pkgver_images_vendor="18.1-20240914"
_pkgver_images_vendor_x86="18.1-20240914"
_pkgver_images_vendor_arm="18.1-20240914"
_pkgver_images_vendor_arm64="18.1-20240914"
pkgname=waydroid-image
pkgver="${_pkgver_images_system//-/_}"
pkgrel=2
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
sha256sums_x86_64=('29f0ceb0846d4c6ac22e37bc942e1f9b0f7df9e640bac92925835201e29f95ae'
                   '8cf6a738d68cc88bc75e2a907a49b3777d8341976f55fb6d918f1e237cf863da')

sha256sums_i686=('7495b0c0685365d8b85aad00f0a504234c383a6f25cd64796a7bf66713612152'
                 'edd71bd8e8583b3cde49580a3db91422609f3108dc1d2ce05aac1dee4be3f570')

sha256sums_armv7h=('b19e2dc52c2d07a1cf8de6a6c4d594bb0ea00d44020014766c13f95dd8140b06'
                   '5c728563b3e9c21d6e38c8a3c9b1376bb62c84dfab3ecf2d2b1dcfdfcdf6744a')

sha256sums_aarch64=('8390f9e55a7ebd73c48f9c71854397bbe2e5fa5d7b560cce6094920e6af3d850'
                    'ffd19e52577e051aaf13139fcc5fc3d23648fe3076f772936f42c9b7ac4efa38')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
