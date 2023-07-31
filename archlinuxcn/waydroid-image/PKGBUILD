# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230729"
_pkgver_images_system_x86="18.1-20230729"
_pkgver_images_system_arm="18.1-20230729"
_pkgver_images_system_arm64="18.1-20230729"
_pkgver_images_vendor="18.1-20230729"
_pkgver_images_vendor_x86="18.1-20230729"
_pkgver_images_vendor_arm="18.1-20230729"
_pkgver_images_vendor_arm64="18.1-20230729"
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
sha256sums_x86_64=('33a4b2af5ecd10b0cb338fb75d722d6ae70e1dc73668c93b9493126b0213b59c'
                   '0f46bed918c76ce282ebeffff6e77f62f4790a9137be51192a6534c92a0c7285')
sha256sums_i686=('3e0dd5176817d1274d31451de2ee780408fe3c7a84425675db84244ede2bcc02'
                 '0777ab4ea9bfce0c0c6d4539aecffc6a63127b18284d6a0dcf2d78a15efde2d7')
sha256sums_armv7h=('57309bf651098df7aa2a824fcc4599e26594c85e9ab1447548a0bcf33d3aa1e6'
                   'f8c771fbae04df293de0de75c6c3cb4e31b2066d1ac26bfba7b3262204414444')
sha256sums_aarch64=('bf477bf3e3b7770290ca4d30e724dd2e606e3a38eed4e7875c41ec6139e61630'
                    '9b1e2816b5e48fad6aa98e70aa083ca5d96fa2db7d2eacde8bd400f85566b61d')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
