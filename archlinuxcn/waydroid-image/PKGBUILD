# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230805"
_pkgver_images_system_x86="18.1-20230805"
_pkgver_images_system_arm="18.1-20230805"
_pkgver_images_system_arm64="18.1-20230805"
_pkgver_images_vendor="18.1-20230805"
_pkgver_images_vendor_x86="18.1-20230805"
_pkgver_images_vendor_arm="18.1-20230805"
_pkgver_images_vendor_arm64="18.1-20230805"
pkgname=waydroid-image
pkgver="${_pkgver_images_system//-/_}"
pkgrel=1
pkgdesc="LineageOS-based Android images for Waydroid"
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url='https://waydro.id'
license=('Apache')
depends=('waydroid')
_srcprefix="https://sourceforge.net/projects/waydroid/files/images"
source_x86_64=("$_srcprefix/system/lineage/waydroid_x86_64/lineage-$_pkgver_images_system-VANILLA-waydroid_x86_64-system.zip"
               "$_srcprefix/vendor/waydroid_x86_64/lineage-$_pkgver_images_vendor-MAINLINE-waydroid_x86_64-vendor.zip")
source_i686=("$_srcprefix/system/lineage/waydroid_x86/lineage-$_pkgver_images_system_x86-VANILLA-waydroid_x86-system.zip"
             "$_srcprefix/vendor/waydroid_x86/lineage-$_pkgver_images_vendor_x86-MAINLINE-waydroid_x86-vendor.zip")
source_armv7h=("$_srcprefix/system/lineage/waydroid_arm/lineage-$_pkgver_images_system_arm-VANILLA-waydroid_arm-system.zip"
               "$_srcprefix/vendor/waydroid_arm/lineage-$_pkgver_images_vendor_arm-MAINLINE-waydroid_arm-vendor.zip")
source_aarch64=("$_srcprefix/system/lineage/waydroid_arm64/lineage-$_pkgver_images_system_arm64-VANILLA-waydroid_arm64-system.zip"
                "$_srcprefix/vendor/waydroid_arm64/lineage-$_pkgver_images_vendor_arm64-MAINLINE-waydroid_arm64-vendor.zip")
sha256sums_x86_64=('50bf718557751a0267dc17fc6937a8a20a1918cd58343ea1bf9970e1a084c67d'
                   'dd92be8cd04dcaffb19f2966e83ca800e23b12e01d1709e88443f4d7984197c5')
sha256sums_i686=('552546b865498a0f65b535f9f0c97c514d3474f76002636925da366505097d67'
                 'ba9189ac1c9a0af3385eeb228445c8381721ffd678ff9d72236bb5c0b99760f0')
sha256sums_armv7h=('0ea4b6d973e9cd4997b82ccb36e48fa1b347ea2614ec5f37154fd55d0c4cf3a1'
                   '30422eb1418301e46fa32169087e0e149907bfb04e4b2fd4b3e689ba86b4e184')
sha256sums_aarch64=('1d64d537864e4819ec98e690fed556807940da966b36f70ed778fe382dfc7ab8'
                    '518390e33947565a2b8d84b26ad565ca01322414bfb31aeafd197c9bb20310ab')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
