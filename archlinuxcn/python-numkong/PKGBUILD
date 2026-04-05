# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=NumKong
pkgname=python-numkong
pkgver=7.4.1
pkgrel=1
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
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ashvardanian/SimSIMD/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('8a5d3c4d9d5adc9658006656fb7465ceabb8f0a176be6f26707864411aecc61d5d228522c68d5b1df49f9fe7eea7ff1bda78ed0fb3b71dd0e45a96ae5e24c6ad')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
