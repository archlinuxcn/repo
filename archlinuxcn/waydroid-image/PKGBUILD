# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20240309"
_pkgver_images_system_x86="18.1-20240309"
_pkgver_images_system_arm="18.1-20240309"
_pkgver_images_system_arm64="18.1-20240309"
_pkgver_images_vendor="18.1-20240309"
_pkgver_images_vendor_x86="18.1-20240309"
_pkgver_images_vendor_arm="18.1-20240309"
_pkgver_images_vendor_arm64="18.1-20240309"
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
sha256sums_x86_64=('f6c007f69d83b7efc59810601025e1ee8f18098b7d1405c7a85d641ffbee87d8'
                   '7dfbf9e85ba03f8501e31a8ddfa2d2b97364f829e841a83d53fb6b2c1b492f63')
sha256sums_i686=('30169df920c272051878954ab84492f8ac77fca4a739f8338d5655cd3596ea91'
                 '0e2c30ced870fbb287f33d2301f0e006f5e51d1bc454474e0b4a0454ba1a2b7b')
sha256sums_armv7h=('6d02d421b9c5410879eb98585182ac4c575c0c5f1e7ec9d51606dab166a5cd5e'
                   'b94edc2a8993347b72969e66dd19b4dd6bde7164d3d60b1045776b6eb9938c81')
sha256sums_aarch64=('fcc6406b74b12ff15df2db4e28e59a91371be01446636b0313a51ced77386826'
                    'd984016eda51284c787ce1fde9755df8fc0aa11ba3a3cc2992b99418c4a1b61e')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
