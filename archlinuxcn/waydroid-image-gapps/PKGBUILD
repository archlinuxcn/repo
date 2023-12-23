# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20231223"
_pkgver_images_vendor="18.1-20231223"

_pkgver_images_system_x86="18.1-20231223"
_pkgver_images_vendor_x86="18.1-20231223"

_pkgver_images_system_arm64="18.1-20231223"
_pkgver_images_vendor_arm64="18.1-20231223"

_pkgver_images_system_arm="18.1-20231223"
_pkgver_images_vendor_arm="18.1-20231223"

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

sha256sums_x86_64=('d5c0af7ed83f9df0f58a7cfe2cef53433f6a6b9498c0a9d2ca9dc27a850eef1d'
                   '050ff5ae04f024b238481d802a4874860394ca793b14ee193b2812c72055d875')
sha256sums_i686=('b44fe21aa2ee436fe5a22fe2a203c99414d53039c2bea27f3245ed49ab14cfbd'
                 '4ac2793b8d5c7a5684632dc4b96344fb0a91827d3d3d9d7787177ba0cabb44cd')
sha256sums_armv7h=('f63bf204aa84161c42bf45c31c0f19f54253e79b37da2f00baeeda1603b433d0'
                   '0cf51efe588ca090bb8642769fc4e41cdc0e975bfb67bc0b4b53b242fd434450')
sha256sums_aarch64=('fbd716a13c293dbb2c732c5e75844fc42141add5db9e0b004948f5eed08041b1'
                    '3eef38ec67a202531537f72181a83a5994a2100c2751bae5694658f5b376461e')
