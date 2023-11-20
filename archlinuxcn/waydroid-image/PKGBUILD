# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20231118"
_pkgver_images_system_x86="18.1-20231118"
_pkgver_images_system_arm="18.1-20231118"
_pkgver_images_system_arm64="18.1-20231118"
_pkgver_images_vendor="18.1-20231118"
_pkgver_images_vendor_x86="18.1-20231118"
_pkgver_images_vendor_arm="18.1-20231118"
_pkgver_images_vendor_arm64="18.1-20231118"
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
sha256sums_x86_64=('0a07f9daf673a9a8eb62150eb77c3e63f5a2dcf266c7eb460f450363fc2a58c6'
                   '3f2f9c3a8cbe74f41bf7ee1090bdcdcf9e3857f83d075ef89a4c02b389d5036b')
sha256sums_i686=('81a1b55878217a027c226e0ccd3b68420f980149edadb5dccd7ffdaadf5ce9e0'
                 '87157de2355a939acf0890eb761b5ae5565120de85849ac6ba0e1ab884f326e6')
sha256sums_armv7h=('c0b9309077b0c4dd55cb71eb507c4d3fe8719fe447a7b70050b14adf16cdd550'
                   '9c07b9f44f73e9b79e6f60cc21153bf81e36686e4ad5ea5d9482ef3b0c7365a0')
sha256sums_aarch64=('b8c2818433b429cf7924a3a873b39406e2a9e3ec350857ea9e532cc7bcea33bb'
                    '48d7c14fc57c08dfdebe2775af42b322d997477bb4d74ce0bd406cf03a642638')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
