# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20240210"
_pkgver_images_vendor="18.1-20240210"

_pkgver_images_system_x86="18.1-20240210"
_pkgver_images_vendor_x86="18.1-20240210"

_pkgver_images_system_arm64="18.1-20240210"
_pkgver_images_vendor_arm64="18.1-20240210"

_pkgver_images_system_arm="18.1-20240210"
_pkgver_images_vendor_arm="18.1-20240210"

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

sha256sums_x86_64=('d021c41c02afe5c3fa6aedcd3870eb3f6964b73539bba25bb6cf05bce7e51cb9'
                   '28aa1d183d3f1aa6576e0ffff98baff2db9e272d5455d0ff5fb046fd9a0e37ef')
sha256sums_i686=('d05a1e60a2570da82b9b752f0fe2c3eb77e2c54aeda57c72418250c0810012a9'
                 '1d40b1205f59f04ba0f77fa8f4c0affbc5d34ab387ae5843bc39e6107ca7453c')
sha256sums_armv7h=('db52369606a1a57c87e90cca0d0642a3ed0182d44c3a7459368f69e40360e74e'
                   '9a276add4c0349f71c7413c7ea0e1dbfb4fef89a1c000b17db44b782efa7a63a')
sha256sums_aarch64=('fcdad85d9eafa5dee60239ac27f855439855edbe954de8c976b6a0d1762fd79e'
                    '742cbde27705124534f8b2a3bc32a091b267de91b2a95b11d6d6aefee478422b')
