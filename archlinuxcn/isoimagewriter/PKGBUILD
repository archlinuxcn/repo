# Maintainer: Luca Weiss <luca (at) z3ntu (dot) xyz>

pkgname=isoimagewriter
pkgver=0.8
pkgrel=1
pkgdesc="Tool to write a .iso file to a USB disk"
arch=("x86_64" "i686")
url="https://community.kde.org/ISOImageWriter"
license=('GPL3')
depends=('qgpgme' 'kiconthemes')
makedepends=('cmake' 'extra-cmake-modules' 'python')
source=("https://download.kde.org/unstable/isoimagewriter/${pkgver}/isoimagewriter-${pkgver}.tar.xz"{,.sig})
sha512sums=('1d5031695647be54e5de10f6243b68bf8d2dc29a7894c8ac69954df353d5baa740290b572c89cd37650718749117f5e3b25dd99b8b374d8ba0376288878f9199'
            'SKIP')
validpgpkeys=('2D1D5B0588357787DE9EE225EC94D18F7F05997E') # Jonathan Riddell

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake \
    ../$pkgname-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DKDE_INSTALL_LIBDIR=lib
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir/" install
}
