# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20231209"
_pkgver_images_system_x86="18.1-20231209"
_pkgver_images_system_arm="18.1-20231209"
_pkgver_images_system_arm64="18.1-20231209"
_pkgver_images_vendor="18.1-20231209"
_pkgver_images_vendor_x86="18.1-20231209"
_pkgver_images_vendor_arm="18.1-20231209"
_pkgver_images_vendor_arm64="18.1-20231209"
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
sha256sums_x86_64=('8db8011bc6fd3aae77c96f1b026b7af1edb9aeb28f26fa529a0677d666555a79'
                   '4b79861332b873d246190f1a76fb6665bdc424aaf31854a0e18e8b0c6d4d3622')
sha256sums_i686=('9372d3f18573cc345ef206e8547082367a1d3b915a5abfbafdeaa35f4ae7b358'
                 '61071ab85a4f9cc29a81e377c2366c3ef6800093a9dbbc18879a7942fe2400ca')
sha256sums_armv7h=('1df2791102848b1d394e99c32f97521c91a62fad6cf6b013f2c115e3f564204e'
                   'accb2e6150397d0bdff7436d5a0dec69fa6796098a41f08e09aa669a6e153ace')
sha256sums_aarch64=('dfd507e9ecb79a26d5e6010fb0e775dcc30adf9b1b2a885efb81015d6d3a1f1b'
                    '6b7800486fd1cdffbd07630967b503e4941024535ba4f5109df11c772d0a92c6')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
