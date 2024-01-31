# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20240127"
_pkgver_images_vendor="18.1-20240127"

_pkgver_images_system_x86="18.1-20240127"
_pkgver_images_vendor_x86="18.1-20240127"

_pkgver_images_system_arm64="18.1-20240127"
_pkgver_images_vendor_arm64="18.1-20240127"

_pkgver_images_system_arm="18.1-20240127"
_pkgver_images_vendor_arm="18.1-20240127"

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

sha256sums_x86_64=('e18c094c6cd2861411c2e78ab66859a13f8b95a0536cd6f57eec1b99ab63ba74'
                   'a8882644ff1650efc920b34aeaa2e67566071c621831449b3a86c491c2b2b836')
sha256sums_i686=('2f937281c94a3065912bb5b3b12dbfd7a03fc50b6b67af8c787cb287abd5039a'
                 'e4f047dc86f93569e373b7bda06d8e3f3f7cb3db30e2b8e74259ded61ed58bd8')
sha256sums_armv7h=('f6dd14566ba896352aac49f130f5a5ac07cf93a35a39861fb0ece4247c0f2caa'
                   '423ff5ec8a4c383bd1750c1fc78e3f8460678d21b4c2858b6e85adb9769677d5')
sha256sums_aarch64=('5c247a88c66e27860b4318f6af45ae7f563c6fc98a31cf2284678535f9366cff'
                    'a259b9a994a4bfce3d009db48a5a1a0da3173133f773f3fe7cb3b22b565e1d93')
