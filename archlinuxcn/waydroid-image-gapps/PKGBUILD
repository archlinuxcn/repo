# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20240217"
_pkgver_images_vendor="18.1-20240217"

_pkgver_images_system_x86="18.1-20240217"
_pkgver_images_vendor_x86="18.1-20240217"

_pkgver_images_system_arm64="18.1-20240217"
_pkgver_images_vendor_arm64="18.1-20240217"

_pkgver_images_system_arm="18.1-20240217"
_pkgver_images_vendor_arm="18.1-20240217"

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

sha256sums_x86_64=('5365a1e65e86df82f39e26dcccf7a249ac135b6b3c62835c085231d3e019992a'
                   '222c94004d6debd0ce52a0b626a885ef8997ff75e8c84974cf090892a829b3d8')
sha256sums_i686=('cc6ab3420e9f8a38fc4357c378985a1b944c9e28c8704e13db104c2687d0a569'
                 'c5d643dd266843b01f38d1db9c76ba0def7e8a7dbd495f90aad672380e72880b')
sha256sums_armv7h=('396349b2def2bfc56fddd06e068cce166837c0568d464e1e8f9640d2b425c315'
                   'e8af751b9b65f6c1453fbdd72b90221ff8042d8f0f55716b064c41984a19d6ae')
sha256sums_aarch64=('b2a7745f8f06695e27db3a9bedc05a597787ee7eac2653847d340cefdb9cf640'
                    '4b3ee46a1de2df66293aa0a197ffb833334a7aca59b80fcccfcf9a242197ebef')
