# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20231202"
_pkgver_images_system_x86="18.1-20231202"
_pkgver_images_system_arm="18.1-20231202"
_pkgver_images_system_arm64="18.1-20231202"
_pkgver_images_vendor="18.1-20231202"
_pkgver_images_vendor_x86="18.1-20231202"
_pkgver_images_vendor_arm="18.1-20231202"
_pkgver_images_vendor_arm64="18.1-20231202"
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
sha256sums_x86_64=('9005187546b298de4c507f0ce374ccfca17824068afebafd37a7618d8849aea3'
                   '6883f92fd859c5807da812a0f11842eedcc20f4fb6fe19215c5c795a5c4b56ba')
sha256sums_i686=('1bc3ead8c4df1f158c663c0def7d8c66d04a2c2503c429393b0d1781bbcbf40f'
                 '59cf0b51f84568775fdc7848331f36dd57ff4b64347293f081736d7ca869d919')
sha256sums_armv7h=('e92c302dd536c3c70c4370902fd9e713010afa3cb0bcddb789a051a7b3259f27'
                   'ad4df78da1bda7a30fbf6bd38ab407c19de7dbe4c778a966dc699cc5ff521a0b')
sha256sums_aarch64=('5c56face84ce8347989761fd30243c5ef49866e0a1e4358dd5390b48b0ab0f3d'
                    'efdacffc128c85c342c64fba5055446e5a388606a71a90fd91beb6a73f4535b3')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
