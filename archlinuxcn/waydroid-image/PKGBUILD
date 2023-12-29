# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20231223"
_pkgver_images_system_x86="18.1-20231223"
_pkgver_images_system_arm="18.1-20231223"
_pkgver_images_system_arm64="18.1-20231223"
_pkgver_images_vendor="18.1-20231223"
_pkgver_images_vendor_x86="18.1-20231223"
_pkgver_images_vendor_arm="18.1-20231223"
_pkgver_images_vendor_arm64="18.1-20231223"
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
sha256sums_x86_64=('2a871b07695368f9b878393f133ed2629c1a00b99199e012e389c6474ba87960'
                   '050ff5ae04f024b238481d802a4874860394ca793b14ee193b2812c72055d875')
sha256sums_i686=('2d014493e7b9fc713ea991bea8443513b8573a0e7771ee855f194b7fd8dcfd4b'
                 '4ac2793b8d5c7a5684632dc4b96344fb0a91827d3d3d9d7787177ba0cabb44cd')
sha256sums_armv7h=('2381c38c063ba13ad2fd522e9e1ba74f15b75d54d3f73d6e661d652044995650'
                   '0cf51efe588ca090bb8642769fc4e41cdc0e975bfb67bc0b4b53b242fd434450')
sha256sums_aarch64=('8a6b4b2f09da31aa7721789dc54550bded154a44776215c71df4d8befeb6daeb'
                    '3eef38ec67a202531537f72181a83a5994a2100c2751bae5694658f5b376461e')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
