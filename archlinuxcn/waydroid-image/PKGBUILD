# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230819"
_pkgver_images_system_x86="18.1-20230819"
_pkgver_images_system_arm="18.1-20230819"
_pkgver_images_system_arm64="18.1-20230819"
_pkgver_images_vendor="18.1-20230819"
_pkgver_images_vendor_x86="18.1-20230819"
_pkgver_images_vendor_arm="18.1-20230819"
_pkgver_images_vendor_arm64="18.1-20230819"
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
sha256sums_x86_64=('8a9411eae47ce28e9df2ea6b40e31cf3a36889f0af3616de9fa6f13676c499b9'
                   '64cc997c23f7cdd52bab359047aedde3d7218430e2dc8c85d28f0896bcd39525')
sha256sums_i686=('9531a12338b5b5efde9d0e42692543e948c4909aa472d71947cbe5bd0012b001'
                 'c9da0eed3cdeb6ec01f4a56f1857950b97d1a5fe526d91f406a109bf20d6e172')
sha256sums_armv7h=('5c956df80f0e9578fb04b11782595d349cc1ce513f7a3248f7dd9cbfff15dbce'
                   '8e9a32a65918295fbae5729da18c4a115069c18bd042e8086eec2f1d924beb76')
sha256sums_aarch64=('dfaa9064bf7e174fb23ede688593392e9e48003770f44aa40714c2648007bfb6'
                    '8d69c092521d23303b9401330ac99ce83b7c7ab3c1edd5e41a895eaadf113d9b')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
