# Maintainer: enamulhasanabid <enamulhabid at gmail dot com>
# Contributor: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20241012"
_pkgver_images_system_x86="18.1-20241012"
_pkgver_images_system_arm="18.1-20241012"
_pkgver_images_system_arm64="18.1-20241012"
_pkgver_images_vendor="18.1-20241012"
_pkgver_images_vendor_x86="18.1-20241012"
_pkgver_images_vendor_arm="18.1-20241012"
_pkgver_images_vendor_arm64="18.1-20241012"
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
sha256sums_x86_64=('082e523d1249e174e07220d55f3893395053d4f621ea3ba4604390be471bc591'
                   '58f675fbe9892db45fcec98547230548ed8841db1bfeb5dafefdcbda9b74c2b0')

sha256sums_i686=('383cf9283886b5f3f1c6946d8462738ca80080e2327315cd8aa6d8b54d7c8dbb'
                 '733bcbd08aeff88b4a97edf2d55b756c6f6991520ae93c8e8ed2de53324ea029')

sha256sums_armv7h=('bb5dbcd994a1c920641e57cda61b9d2a813c4bd5a3d2bdf20f931f99651a17ba'
                   '5a5b1c67904a2467fd93666249fd183ea2a58d9b76cce8349ffa709ecb50c36e')

sha256sums_aarch64=('bc48b4177ab986d05d0182431be6c9d135de9352c02eb7ee5cc3345885f07c5d'
                    'b8da7391ecec5d4a84f6b884b6ef353783e4e24b2d901c460f3dcaa2dac8c471')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
