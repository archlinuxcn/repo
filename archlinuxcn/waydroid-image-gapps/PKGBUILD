# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20230819"
_pkgver_images_vendor="18.1-20230819"

_pkgver_images_system_x86="18.1-20230819"
_pkgver_images_vendor_x86="18.1-20230819"

_pkgver_images_system_arm64="18.1-20230819"
_pkgver_images_vendor_arm64="18.1-20230819"

_pkgver_images_system_arm="18.1-20230819"
_pkgver_images_vendor_arm="18.1-20230819"

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

sha256sums_x86_64=('0c7d0ec93dd994c8e16225633641f13bf629d12785ae88ea406a95b35eae08b4'
                   '64cc997c23f7cdd52bab359047aedde3d7218430e2dc8c85d28f0896bcd39525')
sha256sums_i686=('5b3897ba00c74897e14dd87fe6d1a4f1493a34878da797de519d9c64c7ac9e44'
                 'c9da0eed3cdeb6ec01f4a56f1857950b97d1a5fe526d91f406a109bf20d6e172')
sha256sums_armv7h=('9842504ccded3412fb9f2e50e928ecb9128af1adfc817ab211bd8cd5da2912fc'
                   '8e9a32a65918295fbae5729da18c4a115069c18bd042e8086eec2f1d924beb76')
sha256sums_aarch64=('d4594c48e4de8ba0656500e7debc2cab457a1bdce62f38170aba5f45f773cb72'
                    '8d69c092521d23303b9401330ac99ce83b7c7ab3c1edd5e41a895eaadf113d9b')
