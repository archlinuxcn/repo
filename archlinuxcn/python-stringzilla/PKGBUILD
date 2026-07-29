# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=StringZilla
pkgname=python-stringzilla
pkgver=5.0.5
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
sha512sums=('36c7317303d084e5ce3199fe431d355c5639a4cdaa10a0eb56b1ffa5224cb8e435f259dbac4361d362bc467eee68d558d64de6aa555ffbd656e96039a689d99a')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
