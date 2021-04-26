# Maintainer: Stephan Springer <buzo+arch@Lini.de>
# Contributor: Iwan Timmer <irtimmer@gmail.com>

pkgname=properties-cpp
pkgdesc="A very simple convenience library for handling properties and signals in C++11"
pkgver=0.0.2
_pkgver=0.0.2-6
pkgrel=1
arch=(any)
url="https://launchpad.net/properties-cpp"
license=(LGPL3)
makedepends=(cmake)
source=("https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/${pkgname}/${_pkgver}/${pkgname}_${pkgver}.orig.tar.gz")
sha256sums=(d768aebeadd19aacd99270b9b2288cddb462f7c578ff1d0ea2848bab7b1eb02c)

prepare() {
   # Don't build tests, would need more dependencies.
   echo > "$pkgname-$pkgver"/tests/CMakeLists.txt
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
