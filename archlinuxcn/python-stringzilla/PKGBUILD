# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=StringZilla
pkgname=python-stringzilla
pkgver=4.0.11
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
sha512sums=('32ebd01005596984ec3a73ca437fd089aefce77c4af2723fa475c61d88591d425e89457f7869cbe38c5a133a2f08ea4fbb994f6478fa71a0e77d8d2439bd5cc8')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
