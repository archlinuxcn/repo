# Maintainer: Maxime Gauduin <alucryd@archlinux.org>

pkgname=cereal
pkgver=1.2.2
pkgrel=4
pkgdesc='A C++11 library for serialization'
arch=(x86_64)
url=https://github.com/USCiLab/cereal
license=(BSD)
makedepends=(
  boost
  cmake
  git
)
source=(git+https://github.com/USCiLab/cereal.git#tag=v${pkgver})
sha256sums=(SKIP)

prepare() {
  if [[ -d build ]]; then
    rm -rf build
  fi
  mkdir build
}

build() {
  cd build

  cmake ../cereal \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DSKIP_PORTABILITY_TEST=ON \
    -DTHREAD_SAFE=ON \
    -DWITH_WERROR=OFF
  make
}

package() {
  make DESTDIR="${pkgdir}" -C build install
  install -Dm 644 cereal/LICENSE -t "${pkgdir}"/usr/share/licenses/cereal/
}

# vim: ts=2 sw=2 et:
