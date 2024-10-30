# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=StringZilla
pkgname=python-stringzilla
pkgver=3.10.7
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
sha512sums=('bf4beaf0874df25e9e5eb80c85fcbd77a37f34c51f330336319cfcb0830a5a56ea484dec27ceb3a2922af560b33d7d14859e36907400870f9860350f1698beb0')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
