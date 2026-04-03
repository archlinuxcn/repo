# Maintainer: farwayer <farwayer@gmail.com>
# Co-maintainer: Markus Hartung (harre) <mail@hartmark.se>
# Contributer: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

_system="20.0-20260403"
_vendor="20.0-20260403"

_system_x86="20.0-20260403"
_vendor_x86="20.0-20260403"

_system_arm64="20.0-20260403"
_vendor_arm64="20.0-20260403"

_system_arm="20.0-20260402"
_vendor_arm="20.0-20260403"

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

sha256sums_x86_64=('811ab2dd7ad1b0b4964bddf020fa450275ea1af2d5b0ac10d5ceced0ac1908a3'
                   '24cc7e0d9e28b4ff32b4f097f2fc816a4552ac2070b2422afb28d39ac78d426b')
sha256sums_i686=('2f1f8d96bc43b7c2ad0718c893c9d019e27e481c90316b9aefd50adbb7bf16cb'
                 '03f1dfc41b0f37471843c1f2ecb72bc635e8ddf6ecd80b2c41ec6ef8ebe303a7')
sha256sums_armv7h=('cff0ccc2fbaf875bb06501c507dfc90f8b5a26aabb0e677ca48e754b914c3309'
                   'b81703ff498af328ffe39354a8d9956be51a184fa319e2648964910d35ba9673')
sha256sums_aarch64=('c5e557605887664ab1da6c17ff0032317735a0425b8055ee9073fdbcd00899c2'
                    '1e6d33d464277ea3964e4658001c8882f21325616d6bcc66d473bc9ee1e246c7')
