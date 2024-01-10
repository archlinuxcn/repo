# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20231230"
_pkgver_images_system_x86="18.1-20231230"
_pkgver_images_system_arm="18.1-20231230"
_pkgver_images_system_arm64="18.1-20231230"
_pkgver_images_vendor="18.1-20231230"
_pkgver_images_vendor_x86="18.1-20231230"
_pkgver_images_vendor_arm="18.1-20231230"
_pkgver_images_vendor_arm64="18.1-20231230"
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
sha256sums_x86_64=('d1c1cbb2afc03f3a6f027f11f97b05dabc48e783c91d3d413b2cf1d1d6489c53'
                   'a63ae386ab47164e88873776f5c6275b60a259d190630f1c1cb1023b671609f4')
sha256sums_i686=('91658a0109dced520509d8d89d9ea240dfad40d2496294ed75a24bd8fd6e9b16'
                 '47c88a9ee58b8783dbc671f1e5202b8ecae0ebffe270409866fbfe5075d18cb2')
sha256sums_armv7h=('e1a58f347bbd9614ddae0778cb29ce8d56fb9a6afbd4f8dcd14903370f6c3957'
                   'b932d78a1b7482a56532ee66cf9ae72df6d48daa908615e307a7ff6e1766284d')
sha256sums_aarch64=('4b0ae36453453f019520b90eef85d04335a2323e6db88389f5af2c82e6b187c3'
                    '480a5be2fa335bf50a44676f7f4e01ef7893e0cd99f7dc41ba85b6023706b14e')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
