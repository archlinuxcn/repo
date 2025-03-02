# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=StringZilla
pkgname=python-stringzilla
pkgver=3.12.2
pkgrel=1
pkgdesc='SIMD-accelerated string search, sort, hashes, fingerprints, & edit distances'
arch=('x86_64')
url='https://github.com/ashvardanian/StringZilla'
license=('Apache-2.0')
depends=(
  glibc
  python
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ashvardanian/StringZilla/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('d48069bc4e5c648a67132ddfe30943d3945e92682cd3faab97834164dbb0fa1b8023fca6428d5fd1b4e6a44fd9bcd7a943b4251e54e2dc16337021c5fa0d208f')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
