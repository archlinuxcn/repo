# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="20.0-20250726"
_pkgver_images_vendor="20.0-20250726"

_pkgver_images_system_x86="20.0-20250726"
_pkgver_images_vendor_x86="20.0-20250726"

_pkgver_images_system_arm64="20.0-20250726"
_pkgver_images_vendor_arm64="20.0-20250726"

_pkgver_images_system_arm="20.0-20250726"
_pkgver_images_vendor_arm="20.0-20250726"

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

sha256sums_x86_64=('719f140c857ba26d796715736c8d569d7cc20ca2f3a08e26c23fce224ec9d8c0'
                   '170b5ba38e3fd1a5b7e23b7fc1a5740e3fabfe5e2425837a5f83cbe18f75252e')
sha256sums_i686=('73f3308bd8d63dc4ceba499526117a043207909d0bc6344bc64d64ed96f0c12e'
                 '450a0c5ad919f1e100f7bfe8011e7d5f131de6a11b839320f03a29057a3280d6')
sha256sums_armv7h=('58cdbdaf841d8c19148a8fff52d5b719e093db762943b1012ef273a631100881'
                   '7610f2e6d0a113be4fa46fc7428ad8c11c0913ea09a32babb88ef40956671274')
sha256sums_aarch64=('b95e1c1062aaaa6bf6e101dc411a03ea6362e8079095b8edbed4d93fa87c1f3f'
                    '3079d9e74c49b8ea9bb1aeb379c6cca15daafafb1062eccd323c3ece07922c71')
