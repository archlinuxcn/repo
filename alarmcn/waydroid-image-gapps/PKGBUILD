# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="20.0-20250712"
_pkgver_images_vendor="20.0-20250712"

_pkgver_images_system_x86="20.0-20250712"
_pkgver_images_vendor_x86="20.0-20250712"

_pkgver_images_system_arm64="20.0-20250712"
_pkgver_images_vendor_arm64="20.0-20250712"

_pkgver_images_system_arm="20.0-20250712"
_pkgver_images_vendor_arm="20.0-20250712"

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

sha256sums_x86_64=('ea0fda8376799ebb81e841e29e600e82f076a8c72665ffcd02017fa04cfbd23f'
                   '14863819884119923940abe1a120ef265b4dede77036f5597877cc63e0fd85ee')
sha256sums_i686=('1b3ce0b5a7040f3a8fd8ba76da006aaba2a40cad4eeb5afb0118cae5c4877fae'
                 '9826bc0abdc278390af2fa24a32e7367a4aa799f481d5666b0baed3681e9a51d')
sha256sums_armv7h=('368eb4457fec6400314f23440055d4df28a5a41256e7ee60978b92b463c8e9cd'
                   '75374b15f1d9354a57f6d517d0744ebd87c15b9d29e108f8e8558015ff782d78')
sha256sums_aarch64=('2546550c4e2ba58c94105b9e91f80075f893af8d453fb6e91735c0919cfd7607'
                    '61d5984a502b49c39aee42651a98c0c7cd6a25f755dd35a52a010282a71c6a9c')
