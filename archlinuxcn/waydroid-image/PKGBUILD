# Maintainer: enamulhasanabid <enamulhabid at gmail dot com>
# Contributor: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20241116"
_pkgver_images_system_x86="18.1-20241116"
_pkgver_images_system_arm="18.1-20241116"
_pkgver_images_system_arm64="18.1-20241116"
_pkgver_images_vendor="18.1-20241116"
_pkgver_images_vendor_x86="18.1-20241116"
_pkgver_images_vendor_arm="18.1-20241116"
_pkgver_images_vendor_arm64="18.1-20241116"
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
sha256sums_x86_64=('a99d4414c469daebe75c35dbd808bd5c7c7f0b996d759e53514de73a387f5457'
                   '50b986db59f7f99b36e9b656f57d139ecbf988a7257524bf0988c8d061f21bed')

sha256sums_i686=('9004d6b2ea456897456f90bb6f2a9386f5f40bf1d224b4786f0abb1968879f04'
                 '6cb06d5e2c8ba361dad8bc02a4a2965b4d24a2177e843280d62ffb965fe2ce43')

sha256sums_armv7h=('a22fbd135f8ab4a6b79ee071b63cc88c654a346dd30593aacf8494bcfcecb3ad'
                   '521774b70e35c29d1f5310129f9ed02b02810aeabc943470fc64aa22e96bb7c6')

sha256sums_aarch64=('cd4a6f5390ff649b4ad64ca123ebdcd1aeae4c531a89f2aeebbccc5a782ac03c'
                    'de0408f11ca12356d86846b9a28240c125f36f623107c4c27e171e1515736687')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
