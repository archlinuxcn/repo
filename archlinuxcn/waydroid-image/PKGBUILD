# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230930"
_pkgver_images_system_x86="18.1-20230930"
_pkgver_images_system_arm="18.1-20230930"
_pkgver_images_system_arm64="18.1-20230930"
_pkgver_images_vendor="18.1-20230930"
_pkgver_images_vendor_x86="18.1-20230930"
_pkgver_images_vendor_arm="18.1-20230930"
_pkgver_images_vendor_arm64="18.1-20230930"
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
sha256sums_x86_64=('2282005d1f4112bbc9dd8087325ffee5f2b4ff477277ad06cb603f69c02831ab'
                   '4e32fa3bc90bb1892be33ba32ddb7e4fb67fac5873593a99126a0a9f5174429f')
sha256sums_i686=('7a41c80279a64d7e25c9384538bee2b1a2c3e207b6cceca1fcd152c2e7600539'
                 '1fc120f3a57fd83ff0c3286f55a36934da7f5a00b52ec717d1b9a8d17d0f9e08')
sha256sums_armv7h=('46c4b0204fc0ba713b71c842c8d23a648e8bf1931d9f8495b11db0efbf722f80'
                   'f64a81c0fed3d6f6cecee0defb2b96fb0b540a127bec671eaadb43c0d295e355')
sha256sums_aarch64=('e44036cd4e0b4a3df54621a5d7a74dca048cba5d44a707193a1af6ee8adc9efe'
                    '05b6cf5c3bd4188a37af9f6c74e3120853fef5422a3cb869d84775f885c847d5')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
