# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20231014"
_pkgver_images_vendor="18.1-20231014"

_pkgver_images_system_x86="18.1-20231007"
_pkgver_images_vendor_x86="18.1-20231014"

_pkgver_images_system_arm64="18.1-20230930"
_pkgver_images_vendor_arm64="18.1-20231007"

_pkgver_images_system_arm="18.1-20231007"
_pkgver_images_vendor_arm="18.1-20231014"

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

sha256sums_x86_64=('39c695588adfcd482911233e36db5d7adfb7bea351df256eefd345b95436f2b4'
                   '951c41b4ce007e16387920ea61cb531b882a79d0ae8d0795eb1cc2f790deecc9')
sha256sums_i686=('c9d1d19799ebf1c239772e4fb4fbb266cdc106222906a04219536420d3aeebaa'
                 '92bc1bbc98e2cd06b4f8bbed61154de709fdef8ee3cb63861b476b379a70fd3f')
sha256sums_armv7h=('18c4f4fb27498a689d5ce93720d177f19cbc7f33196e9e34af93e2416248235d'
                   'd2fb78b2e7d3f5b50da6a899aa41e5f9bae84c01a245a178213f1710212517b1')
sha256sums_aarch64=('d0eaa04ba445e3cad4e60ddc3bdf0a0c990a575c96b8e51e686b71721d6cfd0d'
                    '92bdbe349e587056f0a6c38eb24c4fc7dfee2f4acac3802319acbf7eab048a6e')
