# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="20.0-20250719"
_pkgver_images_vendor="20.0-20250719"

_pkgver_images_system_x86="20.0-20250719"
_pkgver_images_vendor_x86="20.0-20250719"

_pkgver_images_system_arm64="20.0-20250719"
_pkgver_images_vendor_arm64="20.0-20250719"

_pkgver_images_system_arm="20.0-20250719"
_pkgver_images_vendor_arm="20.0-20250719"

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

sha256sums_x86_64=('87210410f5ea6fb86dda379430008386a0489280eaf647fd8e3f67701e31535f'
                   'cedb5e69d20aa1c3f25c6d246520cdb8536f5ebaef440b8f40e7898ef99802ad')
sha256sums_i686=('e43f1e0454347f05105445a9cd0ae166591444c7e5333e946ddf4fee41c6043f'
                 'c02628da6f724dbcae5af31883b7484eb80bed326c8eb682803b1d4a642f86c2')
sha256sums_armv7h=('a10df676595f6ebcd7bf3e17f449a6eb9d95b69e7cdc211c7f1872cdf0eab429'
                   '2e26b87334027ae5c3b62a3a6625e6824d1a75a539adca50b210d0a6ce8ff883')
sha256sums_aarch64=('4ab06b170f47af7288870ab0ed4fe0d19281e564af39719599d6967ff2bd800a'
                    '7b068ab5865d0438cbf49031983efdd5a580ae17524762cc249647431382eb03')
