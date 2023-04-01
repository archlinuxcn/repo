# Maintainer: Luca Weiss <luca (at) z3ntu (dot) xyz>

pkgname=isoimagewriter
pkgver=0.9.1
pkgrel=1
pkgdesc="Tool to write a .iso file to a USB disk"
arch=("x86_64" "i686")
url="https://community.kde.org/ISOImageWriter"
license=('GPL3')
depends=('qgpgme' 'kiconthemes' 'kcrash' 'solid')
makedepends=('cmake' 'extra-cmake-modules' 'python')
source=("https://download.kde.org/unstable/isoimagewriter/${pkgver}/isoimagewriter-${pkgver}.tar.xz"{,.sig})
sha512sums=('f989c4bd164e2a34d5b2305eac67f34e2a47056993e30c9d9041679b49eb004b40cdae956d49a0b11a12feff280915f5bcd45e12c8a1f8975d95eb99f36c4b2d'
            'SKIP')
validpgpkeys=('E0A3EB202F8E57528E13E72FD7574483BB57B18D') # Jonathan Esk-Riddell

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
