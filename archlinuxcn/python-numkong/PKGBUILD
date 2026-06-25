# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=NumKong
pkgname=python-numkong
pkgver=7.7.0
pkgrel=2
pkgdesc='A Fast Dot Products & Similarity Metrics for Python using SIMD'
arch=('x86_64')
url='https://github.com/ashvardanian/numkong'
license=('Apache-2.0')
depends=(
  gcc-libs
  glibc
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
provides=(
  python-simsimd
)
replaces=(
  python-simsimd
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ashvardanian/numkong/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('3cc697c7b65e65ad9735c3e5211f3b0e7b86df2469dc56dd19be0323b9e22c939ab69d98828c4071c6a4490140cabd56c2765297a7d5a83bf159d4b957b90b34')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
