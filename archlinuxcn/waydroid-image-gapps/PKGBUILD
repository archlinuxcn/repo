# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20231209"
_pkgver_images_vendor="18.1-20231209"

_pkgver_images_system_x86="18.1-20231209"
_pkgver_images_vendor_x86="18.1-20231209"

_pkgver_images_system_arm64="18.1-20231209"
_pkgver_images_vendor_arm64="18.1-20231209"

_pkgver_images_system_arm="18.1-20231209"
_pkgver_images_vendor_arm="18.1-20231209"

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

sha256sums_x86_64=('685731a22238424c05e9ad0b228ccda71a0dc8a8b43143bc9a2ea755ab0bd285'
                   '4b79861332b873d246190f1a76fb6665bdc424aaf31854a0e18e8b0c6d4d3622')
sha256sums_i686=('052b06a2d455452b505c858e618d3271eb369630c7fc3af333dbcd94ca0d7a3e'
                 '61071ab85a4f9cc29a81e377c2366c3ef6800093a9dbbc18879a7942fe2400ca')
sha256sums_armv7h=('893ca7aa328db9514e17c9643efb78b60f8ea8261b1b46086f46a44c2e44e104'
                   'accb2e6150397d0bdff7436d5a0dec69fa6796098a41f08e09aa669a6e153ace')
sha256sums_aarch64=('3e483521161333a27def04cae55ae95aaf5991114c80b076c81044de93449fa9'
                    '6b7800486fd1cdffbd07630967b503e4941024535ba4f5109df11c772d0a92c6')
