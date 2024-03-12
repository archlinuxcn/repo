# Maintainer: Rocket Aaron <i at rocka dot me>

_repo=uswitch
pkgname=plasma-applet-uswitch
# TODO remove this when new version releases
_ref=440f2d859468aa5a8958766c171ff3f5e01d90f5
pkgver=1.3.0plasma6
pkgrel=1
pkgdesc='Modified version of User Switch plasmoid'
url="https://gitlab.com/divinae/uswitch"
license=('GPL-3.0-only')
arch=('any')
depends=('plasma-workspace')
makedepends=('cmake' 'extra-cmake-modules')
source=("$_repo-$pkgver.tar.gz::https://gitlab.com/divinae/$_repo/-/archive/$_ref/archive.tar.gz"
        "CMakeLists.txt")
sha256sums=('c1752af72c5df6a456de058dd8d5248ea68a312ed3fe3cf821fc15ecb7a08cca'
            '0d48b3dc6b4249ad24468d7d629d3cc26d72cab11dfe51f088a2210f263ec045')

build() {
  local _src="$_repo-$_ref"
  cp "$srcdir/CMakeLists.txt" "$_src"
  cmake -S "$_src" -B build \
    -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
