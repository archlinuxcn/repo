# Maintainer: Luca Weiss <luca (at) z3ntu (dot) xyz>

pkgname=isoimagewriter
pkgver=0.9
pkgrel=1
pkgdesc="Tool to write a .iso file to a USB disk"
arch=("x86_64" "i686")
url="https://community.kde.org/ISOImageWriter"
license=('GPL3')
depends=('qgpgme' 'kiconthemes' 'kcrash' 'solid')
makedepends=('cmake' 'extra-cmake-modules' 'python')
source=("https://download.kde.org/unstable/isoimagewriter/${pkgver}/isoimagewriter-${pkgver}.tar.xz"{,.sig})
sha512sums=('94a05da44b22ae932a79f6bb91c6806047f94e9b0fb4fe5530eb6094664877c47a0581f0858ff4458daca8924a7803a979e74d6538ec8da642403c4ede58688d'
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
