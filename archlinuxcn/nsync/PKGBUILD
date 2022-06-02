# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgname=nsync
pkgver=1.25.0
pkgrel=1
pkgdesc='A C library that exports various synchronization primitives, such as mutexes'
arch=(x86_64)
url='https://github.com/google/nsync'
license=(Apache)
depends=(gcc-libs)
makedepends=(cmake)
source=("https://github.com/google/nsync/archive/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('2be9dbfcce417c7abcc2aa6fee351cd4d292518d692577e74a2c6c05b049e442')

build() {
  cmake -B build -S $pkgname-$pkgver \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=ON
  make -C build
}

check() {
  make -C build test
}

package() {
  make -C build DESTDIR="$pkgdir" install
}
