# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230916"
_pkgver_images_system_x86="18.1-20230916"
_pkgver_images_system_arm="18.1-20230916"
_pkgver_images_system_arm64="18.1-20230916"
_pkgver_images_vendor="18.1-20230916"
_pkgver_images_vendor_x86="18.1-20230916"
_pkgver_images_vendor_arm="18.1-20230916"
_pkgver_images_vendor_arm64="18.1-20230916"
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
sha256sums_x86_64=('52a97fd3d5f56058091140a8f9b980ab62bcb181b2d1c28be2827f3fe0f927fa'
                   '504aa3ce973ed2a7622b8c7a40e6ea7f08071248ee08d97546181410ea0900dd')
sha256sums_i686=('6feb62d4d524aa5b17e15894af2c8776a8e24147e1dfba025f555ffc8f8cea24'
                 '6105cea64ca012a8c6dcf0fc2afa1f7d826e4f9dd68869fbcbc19a38890b74db')
sha256sums_armv7h=('025809b28f99fd55d9a12d49ae260af88061a0c0aef00c3924572d105dc44a02'
                   'f5e0c1a854a13148ed7ca9de3da566955f0bdec3058fd6fc7156c659b3c85178')
sha256sums_aarch64=('cc5603b1a328ccbbb1193422fb3a7f3bb83214d7db2faeb4bb147cbfcc868013'
                    '3a28f225375d2c5eb6d78a523f184f9cb324779164d2313a61ba5e75c0d9f26f')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
