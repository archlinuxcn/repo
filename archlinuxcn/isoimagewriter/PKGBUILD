# Maintainer: Luca Weiss <luca (at) z3ntu (dot) xyz>

pkgname=isoimagewriter
pkgver=0.2
pkgrel=1
pkgdesc="A program to write hybrid ISO files onto a USB disk from Linux, Mac or Windows ready to boot."
arch=("x86_64" "i686")
url="https://community.kde.org/ISOImageWriter"
license=('GPL3')
depends=('ki18n' 'kauth' 'qgpgme' 'kiconthemes' 'kwidgetsaddons')
makedepends=('cmake' 'extra-cmake-modules' 'python')
source=("https://download.kde.org/unstable/isoimagewriter/${pkgver}/isoimagewriter-${pkgver}.tar.xz"{,.sig})
sha512sums=('cec7d67e8255caaaccc14d07da3677a13b8081f599136516b0a31262e20eec884fa738dcc2d3aa1bfd49c00bb6c5bc6c3a62c767b13cdb06799cb53cf1e6ecc1'
            'SKIP')
validpgpkeys=('2D1D5B0588357787DE9EE225EC94D18F7F05997E') # Jonathan Riddell
options=(!buildflags)

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake ../$pkgname-$pkgver -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DKDE_INSTALL_LIBDIR=lib
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir/" install
}
