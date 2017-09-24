# Maintainer: Iwan Timmer <irtimmer@gmail.com>

pkgname=dbus-cpp
pkgdesc="A header-only dbus-binding leveraging C++-11"
pkgver=5.0.0
_pkgver=5.0.0+16.10.20160809
pkgrel=1
arch=('x86_64')
url="https://code.launchpad.net/dbus-cpp"
license=('LGPL3')
depends=('process-cpp' 'dbus' 'libxml2')
makedepends=('cmake' 'gmock' 'properties-cpp' 'boost')
source=("https://launchpad.net/ubuntu/+archive/primary/+files/dbus-cpp_5.0.0+16.10.20160809.orig.tar.gz")
md5sums=('SKIP')

prepare() {
  cd "$srcdir"

  # Don't build tests
  truncate -s 0 tests/CMakeLists.txt
}

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake .. -DCMAKE_INSTALL_LIBDIR=/usr/lib -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DDBUS_CPP_VERSION_MAJOR=5 -DDBUS_CPP_VERSION_MINOR=0 -DDBUS_CPP_VERSION_PATCH=0
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir/" install
}
