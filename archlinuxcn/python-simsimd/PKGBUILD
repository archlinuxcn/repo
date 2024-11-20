# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=SimSIMD
pkgname=python-simsimd
pkgver=6.1.1
pkgrel=1
pkgdesc='A Fast Dot Products & Similarity Metrics for Python using SIMD'
arch=('x86_64')
url='https://github.com/ashvardanian/simsimd'
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
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ashvardanian/SimSIMD/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('338bd6c12647f0231bfa5f1f22538c3ebfa3a838abcbcc86bee21ed8713dd72701f62245e143e3546b6299fd324221b72abd9b2d7041fece5ea379a65ffd95cc')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
