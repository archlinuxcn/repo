# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20230304"
_pkgver_images_vendor="18.1-20230304"

_pkgver_images_system_x86="18.1-20230218"
_pkgver_images_vendor_x86="18.1-20230304"

_pkgver_images_system_arm64="18.1-20230304"
_pkgver_images_vendor_arm64="18.1-20230304"

_pkgver_images_system_arm="18.1-20230304"
_pkgver_images_vendor_arm="18.1-20230304"

pkgname=waydroid-image-gapps
pkgver="${_pkgver_images_system//-/_}"
pkgrel=1
pkgdesc="A container-based approach to boot a full Android system on a regular Linux system (Android image, GAPPS)."
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
license=('Apache')
url='https://github.com/waydroid'
depends=('waydroid')
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

sha256sums_x86_64=('3855aa2c2ef36d89c081c2d948f7d2f20a4af8ff2ba05cd5a0062194558b7081'
                   'e4380e8a8751b173d1cfa13d892cb5e7d5d71620604b5f529f6abae7f97466d2')
sha256sums_i686=('de573f78feb4a14b424af35c4ae8b637d5c5db5bff22cd82951b6331c7511855'
                 '4a1ec222f6e0d289e35e8acecee2395ffd5dcb61811514284b02ee2c01683c5c')
sha256sums_armv7h=('45e6987b367ed58cb67b3c1d5e9cf0bf5f4dba897e3073b7686800df69ec4a13'
                   '4e4ea94a827eb72e9a16a64396a6d95fe5a33daf127729ea0284a0e57a89db8c')
sha256sums_aarch64=('ef741673e861180342328745b03cb6bf0baa87dfa68593f35f24934da66ed510'
                    '5db03885bf7f5621eb707536157fc8e863e8dbea99caf7b80e1708cca563dd5d')
