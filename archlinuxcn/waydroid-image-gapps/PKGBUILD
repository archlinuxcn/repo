# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20231104"
_pkgver_images_vendor="18.1-20231104"

_pkgver_images_system_x86="18.1-20231104"
_pkgver_images_vendor_x86="18.1-20231104"

_pkgver_images_system_arm64="18.1-20231028"
_pkgver_images_vendor_arm64="18.1-20231104"

_pkgver_images_system_arm="18.1-20231104"
_pkgver_images_vendor_arm="18.1-20231104"

pkgname=waydroid-image-gapps
pkgver="${_pkgver_images_system//-/_}"
pkgrel=1
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
                   '3d6fa204c56d7d4eef2898df5d7d8028c39a686aeafa488cbd9c4ef68dded57b')
sha256sums_i686=('b347b3346368c8d213b273d65270571b73c0e3430a537821023109154537f595'
                 'bbad12328f1f5b7ec8705d3ae1eb5629d844fc6c6d6da9435d8fb2fcfecaaeed')
sha256sums_armv7h=('7b8b0972d340c29e043972bfdd13eb89e8da075127f126f87184c7f1601fd941'
                   '8747e2d7fcf59ca3740f3b744a437f542a9aef459ad5918a73f4445ce9f4d7ba')
sha256sums_aarch64=('4812fe0529074aef38d233074a4262ef69b28a49137e8a3e0f6fbdf59bda85bc'
                    'f475aaef8ed62cf53c29bd3977102f5f69ae6a255e53dcb3048e4dd5abdd7a9a')
