# Maintainer: Rocket Aaron <i at rocka dot me>

_repo=uswitch
pkgname=plasma6-applets-uswitch
# TODO remove this when new version releases
_ref=fdb573e4c03d73023f3555968a186c15d4233e8b
pkgver=1.3.0
pkgrel=3
pkgdesc='Modified version of User Switch plasmoid'
url="https://gitlab.com/divinae/uswitch"
license=('GPL-3.0-only')
arch=('any')
depends=('plasma-workspace')
makedepends=('cmake' 'extra-cmake-modules')
source=("$_repo-$pkgver.tar.gz::https://gitlab.com/divinae/$_repo/-/archive/$_ref/archive.tar.gz"
        "CMakeLists.txt")
sha256sums=('2e251c4ee1fca3d173798c64265c89ed477555b26b5195a92ad317596b537466'
            '6a650bb4f2e4781a2b0a33f088cc1dad97f21547cc93b2b7b1b64d0dfbb9f35b')
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
