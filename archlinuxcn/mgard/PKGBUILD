# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=MGARD
pkgname=mgard
pkgver=0.0.0.2
pkgrel=1
pkgdesc='MultiGrid Adaptive Reduction of Data'
license=('Apache')
arch=('x86_64')
url='https://github.com/CODARcode/MGARD'
depends=(
  'gcc-libs'
  'zlib'  
)
makedepends=('cmake')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/CODARcode/MGARD/archive/${pkgver}.tar.gz")
sha256sums=('f18003be4aa639eb2e47fb374951ac8cb64a0fca77d1f385495e7173c2b81e8f')

build() {
  mkdir build && cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_SKIP_INSTALL_RPATH=ON \
        "${srcdir}/${_pkgname}-${pkgver}"
  make
}

check() {
  cd build
  ctest -v
}

package() {
  cd build
  make DESTDIR="${pkgdir}" install
}
# vim:set ts=2 sw=2 et:
