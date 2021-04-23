# Maintainer: Javier Tiá <javier dot tia at gmail dot com>

pkgname=doctest
pkgver=2.4.1
pkgrel=1
pkgdesc='The lightest feature rich C++ single header testing framework'
arch=('any')
url='https://github.com/onqtam/doctest'
license=('MIT')
makedepends=('cmake')
source=("${url}/archive/${pkgver}.tar.gz")
sha256sums=('0a0f0be21ee23e36ff6b8b9d63c06a7792e04cce342e1df3dee0e40d1e21b9f0')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  mkdir build
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  cmake -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DDOCTEST_WITH_TESTS=off \
        -G"Unix Makefiles" \
        ../
  make
}

# check() {
  # cd "${srcdir}/${pkgname}-${pkgver}/build"
  # make
  # ctest -C Release --output-on-failure
# }

package() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  make DESTDIR="${pkgdir}" install
  install -Dm 0644 ../LICENSE.txt \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
