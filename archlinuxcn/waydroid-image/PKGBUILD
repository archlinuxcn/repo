# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20240113"
_pkgver_images_system_x86="18.1-20240113"
_pkgver_images_system_arm="18.1-20240113"
_pkgver_images_system_arm64="18.1-20240113"
_pkgver_images_vendor="18.1-20240113"
_pkgver_images_vendor_x86="18.1-20240113"
_pkgver_images_vendor_arm="18.1-20240113"
_pkgver_images_vendor_arm64="18.1-20240113"
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
sha256sums_x86_64=('d2932561cee8c3cb04b9114470c518644ec707851cc16411d0d1fe3685fc8ce2'
                   '6deea932444a1a2050507a93abe98bec42129cda23eaad82254103d36a12a840')
sha256sums_i686=('33859cc5e38ee7c2acdf9478c8348150ddc8d58ad88caef772a15b0852779bd0'
                 'e62eb9020375707f63ebcda96674251d668338cc2d71027df7fc440f2561d4ed')
sha256sums_armv7h=('3bdd35623e7c2c0b37495e3877473df7a7fcd6bd5805f8dddf3f45a749546c69'
                   '9d0f573a8ab865fe4da854d5aaeed359cde714ebdd73b66d02423260002791d1')
sha256sums_aarch64=('e177147108109c4e52914404a7a68a94c1f6fd4c4c46ac0be56a3e6f22fcd1a8'
                    'e8cf4924c0689be84ed05b1b6d1f5cb6d10b5575ad54f5d3ee952da132a6321b')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
