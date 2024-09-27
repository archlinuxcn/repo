# Maintainer: enamulhasanabid <enamulhabid at gmail dot com>
# Contributor: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20240921"
_pkgver_images_system_x86="18.1-20240921"
_pkgver_images_system_arm="18.1-20240921"
_pkgver_images_system_arm64="18.1-20240921"
_pkgver_images_vendor="18.1-20240921"
_pkgver_images_vendor_x86="18.1-20240921"
_pkgver_images_vendor_arm="18.1-20240921"
_pkgver_images_vendor_arm64="18.1-20240921"
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
sha256sums_x86_64=('aa98076c2d0aa4f8c2b4af082f5809938f226cd0b1af4c0389e0d3f3e4ee7064'
                   '9255f7c8a5823e100339dcde761ea6c85d1d35bb4cdb4b02f5cee7d82d3c1b87')

sha256sums_i686=('d070b20e75b82911f6a1d87a7879d8e2f7d3eb5ff7f5ba6bf10d90d549e0a86b'
                 'b4767c7797b0a6fe66253a4a4b848dc432563fdc76a5a514f8280eda1fb1aece')

sha256sums_armv7h=('39d421989e21056e3df1ceca9ad0e3ce37cf3cb93ba623162174c79bff2d2ed5'
                   '9e76bcebfdf6a352b14a4682f58d5727705b9cf0ad645e69a12e2e6692b10f16')

sha256sums_aarch64=('f0b490494668aadeabaa1c21ece4a658cc78804db88062c0184f4ae41c154a40'
                    'fbd922c24eee801bc6d2c4eb633c8cde0a5ab93c1bfcfc7b06e4b88696e9a47b')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
