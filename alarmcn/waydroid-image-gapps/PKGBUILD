# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_system="20.0-20260302"
_vendor="20.0-20260302"

_system_x86="20.0-20260302"
_vendor_x86="20.0-20260302"

_system_arm64="20.0-20260301"
_vendor_arm64="20.0-20260301"

_system_arm="20.0-20260301"
_vendor_arm="20.0-20260301"

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

sha256sums_x86_64=('22823ddea6112e08dc4ee07678b5473ce85cf2bde88dfb8f977bb508035f4319'
                   '132b67715f7686d4bd47e4a6715fba3275973c1e6a640b7a2dd1055bcba50108')
sha256sums_i686=('3d722999823d5873a7e1f7e5578b7f62f161bc435709648b63e6a6dafaf0168d'
                 'dfdea9ceee00d6290f022a9ca4714681b6aca57c16e927803373db7282f1f508')
sha256sums_armv7h=('94ceed7c93c786d7c06fa1a519b16a12e2e6a4c3d636a6ef7d4f54af9952a4b2'
                   'c4515e753e60fc878ab45fa602836e15bd563b7e2481494fc68599d2722f12d4')
sha256sums_aarch64=('c3b8d7a0d045eea26578e79e6ef3cb7b017c6bb4d68f0f2b3f2987af5d74eec0'
                    '211cbd6fd5964c409830f767ed9f89406e48aaed06370fa8d42cfea210f2a04a')
