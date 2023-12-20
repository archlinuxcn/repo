# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20231216"
_pkgver_images_system_x86="18.1-20231216"
_pkgver_images_system_arm="18.1-20231216"
_pkgver_images_system_arm64="18.1-20231216"
_pkgver_images_vendor="18.1-20231216"
_pkgver_images_vendor_x86="18.1-20231216"
_pkgver_images_vendor_arm="18.1-20231216"
_pkgver_images_vendor_arm64="18.1-20231216"
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
sha256sums_x86_64=('fcb59a26a001dd3926fefafa77d79fd54c46ce7a3bffa427cacfe208e8b56789'
                   'eabcaa0dfb2895c71b338d5a600c278eab7440db105f25b8ab98413d99f1e5f1')
sha256sums_i686=('062f428d870f265a1d21da2cd8cd8092fb08c37e17dbfb8165cf3d18a0404fff'
                 'e316bfd880799a36ec70759cf2982905d8612e3e26aa84b5bb0b95687ced85bf')
sha256sums_armv7h=('79e64e6de7384a9fd877fdafdb215103c38d8042582dda319451e447d12f555c'
                   'a35a9eb042039f976306d3b634d516db853adfc7d5f41c9e35ff1fdea2be9cdc')
sha256sums_aarch64=('f446e880948b4d1e72a706dd445d4f2dc8efda8135706fdf5c0504a7b54bf133'
                    'e86bdb73c32b0374790fca5b694006627dc24ffeb3f2a7be1e93bc01ce4ebf08')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
