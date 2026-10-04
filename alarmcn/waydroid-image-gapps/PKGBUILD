# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_system="20.0-20260927"
_vendor="20.0-20260927"

_system_x86="20.0-20260927"
_vendor_x86="20.0-20260927"

_system_arm64="20.0-20260927"
_vendor_arm64="20.0-20260927"

_system_arm="20.0-20260926"
_vendor_arm="20.0-20260927"

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

sha256sums_x86_64=('1d79df0b17ab8f79d66fd3b5f94500cc02f1abe149cf8caa391380092ede6e2a'
                   'd911b8353f6c807b94790b1c41c67e863a9f3dcd1cf3ec0232351398235afd7a')
sha256sums_i686=('7313b2a9a720c87a561c8de5b7566e4302b97963901a8a6b355c1c3ba88742f0'
                 '99af2f69d5fd2c1f2d3830183f6de9689375833ac082e16cc5c9a94cd953990e')
sha256sums_armv7h=('97df844650a19089c33936b1e2d1c79a9443118d75c7cc22dce1d6ef160d788c'
                   '335c710902148cf6f4edac5e7ab464f1af536deb460eb81facd31b9557cec1e7')
sha256sums_aarch64=('a892171f65209078d44f4b85151143665d89ffecf0e6e1c189908937fca155e8'
                    '20a49c11961a5ac7295320f578764eeab3c982b217f1bfde7473adfc22e747ae')
