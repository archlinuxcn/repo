# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20231007"
_pkgver_images_system_x86="18.1-20231007"
_pkgver_images_system_arm="18.1-20231007"
_pkgver_images_system_arm64="18.1-20231007"
_pkgver_images_vendor="18.1-20231007"
_pkgver_images_vendor_x86="18.1-20231007"
_pkgver_images_vendor_arm="18.1-20231007"
_pkgver_images_vendor_arm64="18.1-20231007"
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
sha256sums_x86_64=('19ae5b09c66a79a607484c52a8e36f689ab189cb12443837720af845a0f4f798'
                   '96341f437261cd477b52bdcbddcd9ae69bcacf93ac480c89ce474587d9494478')
sha256sums_i686=('39811b67667e7663e768f7cd01623d6ee444d7762c9fa5044165d7cceb3b685d'
                 '781084d2de635b1b21e994c2e12aed75d21aaac86e7026da01bb4bf42c37aa19')
sha256sums_armv7h=('5d0314eacdc545f8171289b0b6a61eb5f411b00a5559e7f16f61261ee2379e1d'
                   '148aa58b4f3c54540bef814b219f225f6a70598023e59cceff428ea9f303aa44')
sha256sums_aarch64=('bb3c72df6caf32380d684d9a00d3ae4c3e7489660bde430c827e1cc0e5f0acc9'
                    '92bdbe349e587056f0a6c38eb24c4fc7dfee2f4acac3802319acbf7eab048a6e')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
