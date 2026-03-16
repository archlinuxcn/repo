# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_system="20.0-20260312"
_vendor="20.0-20260312"

_system_x86="20.0-20260312"
_vendor_x86="20.0-20260312"

_system_arm64="20.0-20260312"
_vendor_arm64="20.0-20260312"

_system_arm="20.0-20260312"
_vendor_arm="20.0-20260312"

_all=(
  "$_system"
  "$_vendor"
  "$_system_x86"
  "$_vendor_x86"
  "$_system_arm64"
  "$_vendor_arm64"
  "$_system_arm"
  "$_vendor_arm"
)
_latest="$(printf '%s\n' "${_all[@]}" | sort -V | tail -n1)"
_sf="https://sourceforge.net/projects/waydroid/files/images"

pkgname=waydroid-image-gapps
pkgver="${_latest//-/_}"
pkgrel=1
pkgdesc="A container-based approach to boot a full Android system on a regular Linux system (Android image, GAPPS)."
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
license=('Apache')
url='https://github.com/waydroid'
optdepends=('waydroid')
provides=('waydroid-image')
conflicts=('waydroid-image')
source_x86_64=(
  $_sf/system/lineage/waydroid_x86_64/lineage-$_system-GAPPS-waydroid_x86_64-system.zip
  $_sf/vendor/waydroid_x86_64/lineage-$_vendor-MAINLINE-waydroid_x86_64-vendor.zip
)
source_i686=(
  $_sf/system/lineage/waydroid_x86/lineage-$_system_x86-GAPPS-waydroid_x86-system.zip
  $_sf/vendor/waydroid_x86/lineage-$_vendor_x86-MAINLINE-waydroid_x86-vendor.zip
)
source_armv7h=(
  $_sf/system/lineage/waydroid_arm/lineage-$_system_arm-GAPPS-waydroid_arm-system.zip
  $_sf/vendor/waydroid_arm/lineage-$_vendor_arm-MAINLINE-waydroid_arm-vendor.zip
)
source_aarch64=(
  $_sf/system/lineage/waydroid_arm64/lineage-$_system_arm64-GAPPS-waydroid_arm64-system.zip
  $_sf/vendor/waydroid_arm64/lineage-$_vendor_arm64-MAINLINE-waydroid_arm64-vendor.zip
)

package() {
  install -Dm644 "$srcdir"/*.img -t "$pkgdir/usr/share/waydroid-extra/images"
}

sha256sums_x86_64=('b3ead4820a5c4b8d8fe0eea629e25a93863bceedc398c36fb9eee340fe24bd15'
                   '1697a13fbb189caa9e4d89e62f2659f8c5b6a4eb3e499539acc954e3cc0513f5')
sha256sums_i686=('bd2d42ecf1e2feab94d7cffca86f978cb684625679a222384251a7ac017ec7b0'
                 '1a3de4d8b68ef4928832477f28421b564f079fa37fe6296d2affb668b57a4f96')
sha256sums_armv7h=('ead5835aaaf552390fd6fc6361f20c79caa9b78a1854227659264cea45f943b4'
                   '73476ed8c81709591370f81c4eae755958a46b6ad3a7b062743585857af1e4aa')
sha256sums_aarch64=('53d3aedd4c883c7a0de75eb3e16476e23ca3660b86c4f1a5db25cdb9b9fe1007'
                    '06a8f78137cb2d907fff367a389412b80843892e6dfc15e45a93b3297c719010')
