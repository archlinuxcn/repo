# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20231104"
_pkgver_images_vendor="18.1-20231111"

_pkgver_images_system_x86="18.1-20231111"
_pkgver_images_vendor_x86="18.1-20231111"

_pkgver_images_system_arm64="18.1-20231111"
_pkgver_images_vendor_arm64="18.1-20231104"

_pkgver_images_system_arm="18.1-20231111"
_pkgver_images_vendor_arm="18.1-20231111"

pkgname=waydroid-image-gapps
pkgver="${_pkgver_images_system//-/_}"
pkgrel=2
pkgdesc="A container-based approach to boot a full Android system on a regular Linux system (Android image, GAPPS)."
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
license=('Apache')
url='https://github.com/waydroid'
optdepends=('waydroid')
provides=('waydroid-image')
source_i686=(https://sourceforge.net/projects/waydroid/files/images/system/lineage/waydroid_x86/lineage-$_pkgver_images_system_x86-GAPPS-waydroid_x86-system.zip
  https://sourceforge.net/projects/waydroid/files/images/vendor/waydroid_x86/lineage-$_pkgver_images_vendor_x86-MAINLINE-waydroid_x86-vendor.zip)
source_x86_64=(https://sourceforge.net/projects/waydroid/files/images/system/lineage/waydroid_x86_64/lineage-$_pkgver_images_system-GAPPS-waydroid_x86_64-system.zip
  https://sourceforge.net/projects/waydroid/files/images/vendor/waydroid_x86_64/lineage-$_pkgver_images_vendor-MAINLINE-waydroid_x86_64-vendor.zip)
source_armv7h=(https://sourceforge.net/projects/waydroid/files/images/system/lineage/waydroid_arm/lineage-$_pkgver_images_system_arm-GAPPS-waydroid_arm-system.zip
  https://sourceforge.net/projects/waydroid/files/images/vendor/waydroid_arm/lineage-$_pkgver_images_vendor_arm-MAINLINE-waydroid_arm-vendor.zip)
source_aarch64=(https://sourceforge.net/projects/waydroid/files/images/system/lineage/waydroid_arm64/lineage-$_pkgver_images_system_arm64-GAPPS-waydroid_arm64-system.zip
  https://sourceforge.net/projects/waydroid/files/images/vendor/waydroid_arm64/lineage-$_pkgver_images_vendor_arm64-MAINLINE-waydroid_arm64-vendor.zip)

case "$CARCH" in
  aarch64) _imgarch="arm64" ;;
  armv7h) _imgarch="arm" ;;
  *) _imgarch="$CARCH" ;;
esac

package() {
  install -dm755 "$pkgdir/usr/share/waydroid-extra/images"

  # makepkg have extracted the zips
  mv "$srcdir/system.img" "$pkgdir/usr/share/waydroid-extra/images"
  mv "$srcdir/vendor.img" "$pkgdir/usr/share/waydroid-extra/images"
}

sha256sums_x86_64=('fbf22a96d117cd9ac9c2f9279c1b847e3a45dccdb4d3890e217f8260ddb25f84'
                   '868511c2a5041704b7cafeed57262a87c6177e1b6a4b767aebba7766b9f9f463')
sha256sums_i686=('7392866b43f03b8c3bc53fb42763371f4ede32a74342abbeabe1f4330ad5fb81'
                 '3d5f6ac8f97cec69ce7d25b3ceb40de3d1192fe2928ff5cb7cedc112ed7bcda3')
sha256sums_armv7h=('29f293047909960dd6c0a039246f4b7c82344d0624a38156bb72baa80137a947'
                   'ab092aff30864fcc2ccf6baaee5e04a6e06680c8372d384061d0ed2b448d2c75')
sha256sums_aarch64=('1a1ef11f359a4136a0bd61f1ac362781e563302e7fa53a7822828d16008c0f03'
                    'f475aaef8ed62cf53c29bd3977102f5f69ae6a255e53dcb3048e4dd5abdd7a9a')
