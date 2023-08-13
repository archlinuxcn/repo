# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230812"
_pkgver_images_system_x86="18.1-20230812"
_pkgver_images_system_arm="18.1-20230812"
_pkgver_images_system_arm64="18.1-20230812"
_pkgver_images_vendor="18.1-20230812"
_pkgver_images_vendor_x86="18.1-20230812"
_pkgver_images_vendor_arm="18.1-20230812"
_pkgver_images_vendor_arm64="18.1-20230812"
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
sha256sums_x86_64=('ddc1cf7b067ed5e182cc85d704111e8710c6d4d4c2bf242d5aadbcfe34fc906b'
                   'c06fb3e63511594e866aabb2f57d906f897053bcf138ac0fdf0d124c0514c45d')
sha256sums_i686=('8dcf0d1d3f93c3a2b0ae24f7563ea77936bc8ce57eceaef01be8ad7ea6d6715c'
                 'ad75db9ae03241d6431ef9a6482b44823e6c5a03cfad72a798f731152315e86c')
sha256sums_armv7h=('29f617d21a248cd95868b67c2660b3908d4e96ffcdd98c1969ba1d04cc9b32a5'
                   '8e1ebae1f3a98b114713fb3122b3d7c10c51c2f7abb54a50641f364dddf2959c')
sha256sums_aarch64=('957682c4ab677553308a0a2db49d258039c82172ea2a4af6a06adfdbfc2f94ab'
                    'b9de490aee1a2cc1f9fd3b01a3910142a356253cbbc72c5fcdc98390f8ae706c')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
