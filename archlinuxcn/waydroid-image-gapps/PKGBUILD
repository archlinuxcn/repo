# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20231007"
_pkgver_images_vendor="18.1-20231007"

_pkgver_images_system_x86="18.1-20231007"
_pkgver_images_vendor_x86="18.1-20231007"

_pkgver_images_system_arm64="18.1-20230930"
_pkgver_images_vendor_arm64="18.1-20231007"

_pkgver_images_system_arm="18.1-20231007"
_pkgver_images_vendor_arm="18.1-20231007"

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

sha256sums_x86_64=('e2574dbb720521d9e8d797c4602b9d76e4ab215e8bd527bf028be21164cc78f2'
                   '96341f437261cd477b52bdcbddcd9ae69bcacf93ac480c89ce474587d9494478')
sha256sums_i686=('c9d1d19799ebf1c239772e4fb4fbb266cdc106222906a04219536420d3aeebaa'
                 '781084d2de635b1b21e994c2e12aed75d21aaac86e7026da01bb4bf42c37aa19')
sha256sums_armv7h=('18c4f4fb27498a689d5ce93720d177f19cbc7f33196e9e34af93e2416248235d'
                   '148aa58b4f3c54540bef814b219f225f6a70598023e59cceff428ea9f303aa44')
sha256sums_aarch64=('d0eaa04ba445e3cad4e60ddc3bdf0a0c990a575c96b8e51e686b71721d6cfd0d'
                    '92bdbe349e587056f0a6c38eb24c4fc7dfee2f4acac3802319acbf7eab048a6e')
