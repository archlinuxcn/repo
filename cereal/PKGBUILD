# Maintainer: Maxime Gauduin <alucryd@archlinux.org>

pkgname=cereal
pkgver=1.2.2
pkgrel=2
pkgdesc='A C++11 library for serialization'
arch=('i686' 'x86_64')
url='https://github.com/USCiLab/cereal'
license=('BSD')
depends=('')
makedepends=('boost' 'cmake' 'gcc-multilib')
source=("cereal-${pkgver}.tar.gz::https://github.com/USCiLab/cereal/archive/v${pkgver}.tar.gz")
sha256sums=('1921f26d2e1daf9132da3c432e2fd02093ecaedf846e65d7679ddf868c7289c4')

prepare() {
  cd cereal-${pkgver}

  if [[ -d build ]]; then
    rm -rf build
  fi
  mkdir build
}

build() {
  cd cereal-${pkgver}/build

  cmake .. \
    -DCMAKE_BUILD_TYPE='Release' \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS -Wno-unused-variable -Wno-implicit-fallthrough"
  make
}

package() {
  cd cereal-${pkgver}/build

  make DESTDIR="${pkgdir}" install

  install -Dm 644 ../LICENSE -t "${pkgdir}"/usr/share/licenses/cereal/
}

# vim: ts=2 sw=2 et:
