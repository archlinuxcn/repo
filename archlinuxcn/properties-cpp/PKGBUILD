# Maintainer: Stephan Springer <buzo+arch@Lini.de>
# Contributor: Iwan Timmer <irtimmer@gmail.com>

pkgname=properties-cpp
pkgdesc="A very simple convenience library for handling properties and signals in C++11"
pkgver=0.0.3
_pkgver="$pkgver"-1
pkgrel=1
arch=(any)
url="https://launchpad.net/properties-cpp"
license=(LGPL3)
makedepends=(cmake doxygen graphviz)
source=("https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/${pkgname}/${_pkgver}/${pkgname}_${pkgver}.orig.tar.gz")
sha256sums=('62730a43c15dfb8dd28beca8852d7b11f64a6db72f47953bee78b31b9d9b3069')

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
