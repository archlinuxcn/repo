# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=SimSIMD
pkgname=python-simsimd
pkgver=6.3.4
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
sha512sums=('4954312f52268b8e9e20e36160ac8996272f3bbe65fa3398b7912d53c7940112481cc1f36782ae0e59080b71a799245bf6b3d215ed438c66ea5d1d4e03cdb900')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
