# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20240120"
_pkgver_images_system_x86="18.1-20240120"
_pkgver_images_system_arm="18.1-20240120"
_pkgver_images_system_arm64="18.1-20240120"
_pkgver_images_vendor="18.1-20240120"
_pkgver_images_vendor_x86="18.1-20240120"
_pkgver_images_vendor_arm="18.1-20240120"
_pkgver_images_vendor_arm64="18.1-20240120"
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
sha256sums_x86_64=('ba4dde061b9a462f2e063a3f365e0890b1b9146dfc3bb524f7dd25c0784f9854'
                   '899480c34c2ff2384b22856e97c191189180eefff7e4b74ed00365b320a46ea1')
sha256sums_i686=('36e1762aa2f537c986d7e7c3d7ea6773571073bd42212a42508abcea1ea8fa43'
                 '63cc0f5fc2fc012326b37a57abb19ad74a38405be03b942f100b86007a1f1b71')
sha256sums_armv7h=('2a39d1b6afa3aa069452612523a318f4538b49f8ced48396319861e1ab4a97b6'
                   'cb3afe9cf8fba32208fc68565cec062af1ba052489b5bfbbb04879b57a0d079c')
sha256sums_aarch64=('3b3f65a5394ef1161651ee230764df564f5fd287437ff4cc224ed113049b5ae8'
                    'ad5137ea3f75311ad95cd10d59e18670b2f5180a25791c842dedb539fee776a5')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
