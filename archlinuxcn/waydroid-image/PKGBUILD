# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20240323"
_pkgver_images_system_x86="18.1-20240323"
_pkgver_images_system_arm="18.1-20240323"
_pkgver_images_system_arm64="18.1-20240323"
_pkgver_images_vendor="18.1-20240323"
_pkgver_images_vendor_x86="18.1-20240323"
_pkgver_images_vendor_arm="18.1-20240323"
_pkgver_images_vendor_arm64="18.1-20240323"
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
sha256sums_x86_64=('08b207694899b1fbbbb509a4d8fa81d07822fb63e4736204e115f7a2d6df6973'
                   'c3e3e60350d4870342a140c7b4ca5980ae260cb7836d5abf7817d9a87a582f52')
sha256sums_i686=('00df1639a5536367a272c2b6c12b031dfbaecbb89f684c37a8af709281d9a799'
                 '397c960d6bf91db4c26f891f9d5150db6e1e2f62f45eec7f3e096d6331ec66c7')
sha256sums_armv7h=('aab2d12a1953fc4549be02f4f18fe051175ad021662f76592940047f4a992757'
                   'f42680598ffbe5e9f9eed1930fdbcc79b0521d704d6fe0bf93c160c6e9bd078b')
sha256sums_aarch64=('e2addb023b5567871a723193ee2578c9e486da76728b04351f928c14dad93e02'
                    'bdb9ef1ae601646668afebeb60a905de6b95c6fdf38acc0887485121008a7ec2')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
