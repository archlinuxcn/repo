# Maintainer: Iwan Timmer <irtimmer@gmail.com>

pkgname=properties-cpp
pkgdesc="A very simple convenience library for handling properties and signals in C++11"
pkgver=0.0.1
_pkgver=0.0.1+14.10.20140730
pkgrel=1
arch=('any')
url="https://launchpad.net/properties-cpp"
license=('LGPL3')
makedepends=('cmake')
source=("https://launchpad.net/ubuntu/+archive/primary/+files/properties-cpp_$_pkgver.orig.tar.gz")
md5sums=('449f95cc864ebe38a35848885ca1cb4b')

prepare() {
  cd "$srcdir/${pkgname}-${_pkgver}"

  # Don't build tests
  truncate -s 0 tests/CMakeLists.txt
}

build() {
  mkdir -p "$srcdir/${pkgname}-${_pkgver}/build"
  cd "$srcdir/${pkgname}-${_pkgver}/build"

  cmake .. -DCMAKE_INSTALL_LIBDIR=/usr/lib -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release
  make
}

package() {
  cd "$srcdir/${pkgname}-${_pkgver}/build"

  make DESTDIR="$pkgdir/" install
}
