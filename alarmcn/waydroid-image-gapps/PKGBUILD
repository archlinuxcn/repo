# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_pkgver_images_system="20.0-20250705"
_pkgver_images_vendor="20.0-20250705"

_pkgver_images_system_x86="20.0-20250705"
_pkgver_images_vendor_x86="20.0-20250705"

_pkgver_images_system_arm64="20.0-20250705"
_pkgver_images_vendor_arm64="20.0-20250705"

_pkgver_images_system_arm="20.0-20250705"
_pkgver_images_vendor_arm="20.0-20250705"

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

sha256sums_x86_64=('3a936b4602069d22eba0aac063fcb0e8b76c063586d8e4746996fcb26f21cc56'
                   'c989fa0c68b5ff7235e6b6fe6044c19e6ef960d9684e653cd4db3ef912b14188')
sha256sums_i686=('763b136d119eb0a4a43e40c34960e825a3cdc288fd4294abd86298ac998623f5'
                 'b2ac450059a6c15ba47917f0ee2347af03e5d10eadf4ce6d89e7bb543cef1a07')
sha256sums_armv7h=('de4dd56791049c687999d41aab0edccd31fbe0fda182d0e4bc0f730bc3787fc7'
                   '5d19854079ee7456010da5859edf7c2199e20b33aadbd6ab79864195fb5c64dd')
sha256sums_aarch64=('a0cfae085811a605cedbd9812ea7b254d064da7f6c3bc38770f5f6060ff47267'
                    '102862f395011e2215f07910df3148bdd060fdffaf6df6a2de5c62286e5f783f')
