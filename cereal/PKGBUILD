# Maintainer: Maxime Gauduin <alucryd@archlinux.org>

pkgname=cereal
pkgver=1.2.2
pkgrel=3
pkgdesc='A C++11 library for serialization'
arch=('x86_64')
url='https://github.com/USCiLab/cereal'
license=('BSD')
depends=('')
makedepends=('boost' 'cmake')
source=("cereal-${pkgver}.tar.gz::https://github.com/USCiLab/cereal/archive/v${pkgver}.tar.gz")
sha256sums=('1921f26d2e1daf9132da3c432e2fd02093ecaedf846e65d7679ddf868c7289c4')

prepare() {
  if [[ -d build ]]; then
    rm -rf build
  fi
  mkdir build
}

build() {
  cd build

  cmake ../cereal-${pkgver} \
    -DCMAKE_BUILD_TYPE='Release' \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -DSKIP_PORTABILITY_TEST='ON' \
    -DTHREAD_SAFE='ON' \
    -DWITH_WERROR='OFF'
  make
}

package() {
  make DESTDIR="${pkgdir}" -C build install
  install -Dm 644 cereal-${pkgver}/LICENSE -t "${pkgdir}"/usr/share/licenses/cereal/
}

# vim: ts=2 sw=2 et:
