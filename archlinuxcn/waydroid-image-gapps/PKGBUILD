# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="18.1-20240224"
_pkgver_images_vendor="18.1-20240224"

_pkgver_images_system_x86="18.1-20240224"
_pkgver_images_vendor_x86="18.1-20240224"

_pkgver_images_system_arm64="18.1-20240224"
_pkgver_images_vendor_arm64="18.1-20240224"

_pkgver_images_system_arm="18.1-20240224"
_pkgver_images_vendor_arm="18.1-20240224"

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

sha256sums_x86_64=('9ac5727051c543b0eca80e2318e45ebe1894a0f43025397fcc99832c03ff7678'
                   '392f0d9aec184e5b4e9970ff3ae98cdb1356297b5727aa7a4ada1888094648f9')
sha256sums_i686=('a5bb7b2f820e898fd9b1f696bfc65e1fd759cf3c0f5d19b931b377d114aff5a1'
                 '6ea861d6c1b13b024f9f162c8a92eb1b14e9e46de286d7085428ddf66763ea3e')
sha256sums_armv7h=('e731a18da4bf22c753cd75bfc1c5854589f55d7d9e7e5cfda24587427ebd4014'
                   '5c3a21dbe2acb2e330677154da98ebd25b59dd4b2fd6521a43759caf45fd29f0')
sha256sums_aarch64=('bfc1e1442658166f30b692e88ec25f6e3aac29c899e3ef60ebe6a1132c3fdf43'
                    'e40a5d247916100c6a435fa5624501c49fc2a36099f468cdadd117b38943e9f0')
