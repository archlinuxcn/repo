# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20231216"
_pkgver_images_vendor="18.1-20231216"

_pkgver_images_system_x86="18.1-20231216"
_pkgver_images_vendor_x86="18.1-20231216"

_pkgver_images_system_arm64="18.1-20231209"
_pkgver_images_vendor_arm64="18.1-20231216"

_pkgver_images_system_arm="18.1-20231216"
_pkgver_images_vendor_arm="18.1-20231216"

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

sha256sums_x86_64=('c9cf3be3c2d2b8ce2228f82b4c5707c815429a17d10033fa7f0c093317bcd95c'
                   'eabcaa0dfb2895c71b338d5a600c278eab7440db105f25b8ab98413d99f1e5f1')
sha256sums_i686=('d04b39817c02e7338e5399c3ad2e5e7c519fe9c5d3029a46416e1cefd8624169'
                 'e316bfd880799a36ec70759cf2982905d8612e3e26aa84b5bb0b95687ced85bf')
sha256sums_armv7h=('36ebe8ff2facc9d1561e5fd90ee00b7663885edf7aaf3ff351e700240e4eb343'
                   'a35a9eb042039f976306d3b634d516db853adfc7d5f41c9e35ff1fdea2be9cdc')
sha256sums_aarch64=('3e483521161333a27def04cae55ae95aaf5991114c80b076c81044de93449fa9'
                    'e86bdb73c32b0374790fca5b694006627dc24ffeb3f2a7be1e93bc01ce4ebf08')
