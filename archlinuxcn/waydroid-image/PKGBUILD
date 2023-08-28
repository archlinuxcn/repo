# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230826"
_pkgver_images_system_x86="18.1-20230826"
_pkgver_images_system_arm="18.1-20230826"
_pkgver_images_system_arm64="18.1-20230826"
_pkgver_images_vendor="18.1-20230826"
_pkgver_images_vendor_x86="18.1-20230826"
_pkgver_images_vendor_arm="18.1-20230826"
_pkgver_images_vendor_arm64="18.1-20230826"
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
sha256sums_x86_64=('b77dfa312a2817e2d04af0f39dd1a8c28904bd29bdfb06a9aac127d385fe8b3f'
                   '1bd8fa041df938756b95a7884b6b82870670c8f27268a1245259073f99981326')
sha256sums_i686=('4ffe5e916e41549315fe7d240ceeb28a1a85ab6240b436dc48fa25096983e18f'
                 'd75dca1034e85f6018f26c985374eaea98ea28712ba6441abd7caaf1b427c6a5')
sha256sums_armv7h=('e01dbc0e66a18b03692bd5d921758f43ee6bca3d40e0fa28cde2664ba57e9958'
                   'f68432c136fbac15c76eac64268e46876732e82e4f620af7f73b3cf3f6c2d612')
sha256sums_aarch64=('1c93ddb57ac8ea174da2af1f53f56bebd18b44ea5c9966e390642b9748da9c6b'
                    'f1752f2818bbdda8fa6738f59dc4590b37f063341b3cc91851e29daf1c018801')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
