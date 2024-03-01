# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20240224"
_pkgver_images_system_x86="18.1-20240224"
_pkgver_images_system_arm="18.1-20240224"
_pkgver_images_system_arm64="18.1-20240224"
_pkgver_images_vendor="18.1-20240224"
_pkgver_images_vendor_x86="18.1-20240224"
_pkgver_images_vendor_arm="18.1-20240224"
_pkgver_images_vendor_arm64="18.1-20240224"
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
sha256sums_x86_64=('440e29ea36c97b5d78045a18e0b3584ec870332df8b24fd200ccd659fb7fa925'
                   '392f0d9aec184e5b4e9970ff3ae98cdb1356297b5727aa7a4ada1888094648f9')
sha256sums_i686=('dea021d13a0ee16d8fff2e064f0a67e9eb0fa92648381d7f244bf96158d7b854'
                 '6ea861d6c1b13b024f9f162c8a92eb1b14e9e46de286d7085428ddf66763ea3e')
sha256sums_armv7h=('746b861788a65dc68bfc051beea66cde1550b1469ae01d4850d77bdbcb21fd54'
                   '5c3a21dbe2acb2e330677154da98ebd25b59dd4b2fd6521a43759caf45fd29f0')
sha256sums_aarch64=('a63f937fa86551accf26355de1e36fc6eadb58976c3d73933b90214c13e07083'
                    'e40a5d247916100c6a435fa5624501c49fc2a36099f468cdadd117b38943e9f0')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
