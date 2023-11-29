# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20231125"
_pkgver_images_system_x86="18.1-20231125"
_pkgver_images_system_arm="18.1-20231125"
_pkgver_images_system_arm64="18.1-20231125"
_pkgver_images_vendor="18.1-20231125"
_pkgver_images_vendor_x86="18.1-20231125"
_pkgver_images_vendor_arm="18.1-20231125"
_pkgver_images_vendor_arm64="18.1-20231125"
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
sha256sums_x86_64=('faebe8d4af575a3f8b724ed2c4a7138f991bbf22cc5870a3849249f3597e59dc'
                   'ae567a7b76587267ce4a7353b0b5f04228965dbd765dc861f26a8ad48609cbaa')
sha256sums_i686=('f27367957627f298f37e51e998390e5e5597f421434dad1d64235b8e5b528b1c'
                 'f855dd25575d2af6d1e1285170bb8d855b2083e57646f823d0e8648305133e51')
sha256sums_armv7h=('3d51f469ea2686c3e7d39c64ec9de4d9c521e3aa1a225bca2977362d009c9ff7'
                   'ed63499d6daa6948a226aed6464ef52c42aa7ca99266a6cef40b7ec2815016b0')
sha256sums_aarch64=('1025860490a8e97d1534bc51dee3eaacfb1580e4b7456a26ef739342d49ff5c6'
                    '8401829ef5126a63eaa75b7cdf6ad5aedcd329e41ab1af2585b3a8a3d1fd55af')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
