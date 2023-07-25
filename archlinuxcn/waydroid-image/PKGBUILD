# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230723"
_pkgver_images_system_x86="18.1-20230723"
_pkgver_images_system_arm="18.1-20230723"
_pkgver_images_system_arm64="18.1-20230723"
_pkgver_images_vendor="18.1-20230723"
_pkgver_images_vendor_x86="18.1-20230723"
_pkgver_images_vendor_arm="18.1-20230723"
_pkgver_images_vendor_arm64="18.1-20230723"
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
sha256sums_x86_64=('d167a13bbe1eeee39d39b08e0c6af06f3ff76ec7d7786c53ade0af03aa740f20'
                   'a77772f2ec70db8bf22ea9b5f117a8dfffbf127eb044c75b3d208f6f93d1271b')
sha256sums_i686=('372e8866cb7775c9f587e01630d4e2a4bbed7e50f9297a21bf4eb88844311ed3'
                 'b476cc32ac232367deb8becbc19b8d5dfe25a4b1a567ba77ce04578ce476ad96')
sha256sums_armv7h=('743db7f29825e1b5fdb0a8c2bfdeea27b5da16fe67c9c89c17f9ae98f949ae4c'
                   'a7e7bd503a458efea3a233761453e0a4da7be0147b7fa986b8feb08956cadf2c')
sha256sums_aarch64=('b07acb64efad8d588b168899c0c76a817cd09d4e19bfc90a7332c6ee0db452ff'
                    '4c6023d252bf8d87e29c02fac5bd2d13bd74511d65929e42e3b7fe03094bd870')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
