# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20231118"
_pkgver_images_vendor="18.1-20231118"

_pkgver_images_system_x86="18.1-20231118"
_pkgver_images_vendor_x86="18.1-20231118"

_pkgver_images_system_arm64="18.1-20231125"
_pkgver_images_vendor_arm64="18.1-20231125"

_pkgver_images_system_arm="18.1-20231125"
_pkgver_images_vendor_arm="18.1-20231125"

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

sha256sums_x86_64=('9be6edded7bdf32a13a7492afe79f540ad1258b2dcadb73bfabdbe7e916a6b4b'
                   '3f2f9c3a8cbe74f41bf7ee1090bdcdcf9e3857f83d075ef89a4c02b389d5036b')
sha256sums_i686=('dbea819475662ff1b583e5f8dc90428fc624bfbf4a753e5d35270b2722f7fe5c'
                 '87157de2355a939acf0890eb761b5ae5565120de85849ac6ba0e1ab884f326e6')
sha256sums_armv7h=('4f4d645900955eee0bef79ead5b838b59b895700e2c4cb4b994bb67274b7c388'
                   'ed63499d6daa6948a226aed6464ef52c42aa7ca99266a6cef40b7ec2815016b0')
sha256sums_aarch64=('62eccc6e6c42e2edeb3b54293532f3a1f4f7f2ff9ed4c5aa20d2ecba69a6a650'
                    '8401829ef5126a63eaa75b7cdf6ad5aedcd329e41ab1af2585b3a8a3d1fd55af')
