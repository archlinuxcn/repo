# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20231230"
_pkgver_images_vendor="18.1-20231230"

_pkgver_images_system_x86="18.1-20231230"
_pkgver_images_vendor_x86="18.1-20231230"

_pkgver_images_system_arm64="18.1-20231230"
_pkgver_images_vendor_arm64="18.1-20231230"

_pkgver_images_system_arm="18.1-20231230"
_pkgver_images_vendor_arm="18.1-20231230"

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

sha256sums_x86_64=('5869fb138979661606d2b1aad61fe32287d3de0c70ca827bd8e3300f104dac1d'
                   'a63ae386ab47164e88873776f5c6275b60a259d190630f1c1cb1023b671609f4')
sha256sums_i686=('0595d3ae6d1972a91c1dc5933e18feae6469c187909427089e3a443f46563128'
                 '47c88a9ee58b8783dbc671f1e5202b8ecae0ebffe270409866fbfe5075d18cb2')
sha256sums_armv7h=('e7be028144d24c59238d7c353c923804eb310efe27a1f1f944a8a2246de026c2'
                   'b932d78a1b7482a56532ee66cf9ae72df6d48daa908615e307a7ff6e1766284d')
sha256sums_aarch64=('a0760bdbd12f19db2aab68f4f2b9269308c85093cae37e8cb9ea993df568d196'
                    '480a5be2fa335bf50a44676f7f4e01ef7893e0cd99f7dc41ba85b6023706b14e')
