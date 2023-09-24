# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230923"
_pkgver_images_system_x86="18.1-20230923"
_pkgver_images_system_arm="18.1-20230923"
_pkgver_images_system_arm64="18.1-20230923"
_pkgver_images_vendor="18.1-20230923"
_pkgver_images_vendor_x86="18.1-20230923"
_pkgver_images_vendor_arm="18.1-20230923"
_pkgver_images_vendor_arm64="18.1-20230923"
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
sha256sums_x86_64=('9072cf5742f3f78fd705c8854bec6998e14a8fc6af7e0d35113172d150776e50'
                   'ee2b90c00218100ce966d1b5fe3cf9b81f9e803034ebaebeb919ce97b9eeb548')
sha256sums_i686=('fdde16c8e7b86ad0f504b2b1ab4b4a6927536f787515dceaad4c66daa9729224'
                 '67ebc39c12d7972d39b813b1e114a1254773a72568b3c3f5222dafed1ddd295c')
sha256sums_armv7h=('04fd285416269126862e90e91635830a164122584918906ffe0212f6af029bcf'
                   'd4a0181d5b5dc36f15191669584e9b0f7859cf00fce2802b2fad38f97b8e48d0')
sha256sums_aarch64=('56836fe3f5c1c11e38f49bf3c82b78bbe794c3d0031bdd5aa2e077c9862298f6'
                    '77ffb43fd32e8aeee93e3006dcff3da6af8e649e94d0e9f30058fd190b162876')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
