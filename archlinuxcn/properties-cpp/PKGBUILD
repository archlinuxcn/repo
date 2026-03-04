# Maintainer: Stephan Springer <buzo+arch@Lini.de>
# Contributor: Iwan Timmer <irtimmer@gmail.com>

pkgname=properties-cpp
pkgdesc="A very simple convenience library for handling properties and signals in C++11"
pkgver=0.0.4
_pkgver="$pkgver"-1
pkgrel=1
arch=(any)
url="https://launchpad.net/properties-cpp"
license=(LGPL-3.0-only)
makedepends=(cmake doxygen graphviz)
source=("https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/${pkgname}/${_pkgver}/${pkgname}_${pkgver}.orig.tar.bz2")
sha256sums=('572444a88d4709b12adce122ee9ab67690bc72306b8078b4dfebd221e596aaba')

prepare() {
  # don't build tests, would need more dependencies
  echo > "$pkgname-$pkgver"/tests/CMakeLists.txt
  # disable coverage report
  sed -i '/^find_package(CoverageReport)/,$d' "$pkgname-$pkgver"/CMakeLists.txt
}

build() {
  cmake -B build -S "$pkgname-$pkgver" \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
