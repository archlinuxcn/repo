# Maintainer: Luca Weiss <luca (at) z3ntu (dot) xyz>

pkgname=mtxclient
pkgver=0.6.2
pkgrel=1
pkgdesc="Client API library for Matrix, built on top of Boost.Asio"
arch=('x86_64')
url="https://github.com/Nheko-Reborn/mtxclient"
license=('MIT')
depends=('libolm' 'libsodium' 'openssl' 'boost-libs' 'libevent' 'spdlog' 'coeurl')
makedepends=('cmake' 'nlohmann-json' 'boost')
source=("$pkgname-$pkgver.tar.gz::https://github.com/Nheko-Reborn/mtxclient/archive/v$pkgver.tar.gz")
sha256sums=('97e41340c3f03db8a7625dcd54f6c6a3c8726c7b7226630727fea7d2bb2213bf')

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake ../$pkgname-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DBUILD_LIB_TESTS=OFF \
    -DBUILD_LIB_EXAMPLES=OFF \
    -DBUILD_SHARED_LIBS=ON
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
  install -Dm644 ../$pkgname-$pkgver/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
