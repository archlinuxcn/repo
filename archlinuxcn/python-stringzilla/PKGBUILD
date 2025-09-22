# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=StringZilla
pkgname=python-stringzilla
pkgver=4.0.14
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
sha512sums=('3ac917dee288742c9e5a9f5cb9923ec79f0dd0b209bd84698649caf8362e051eca0afb8a01df04b86ad7b9d2d5a922e3456e2e7da64c33b9b83d9aaa61788724')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
