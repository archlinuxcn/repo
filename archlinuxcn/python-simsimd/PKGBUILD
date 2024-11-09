# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=SimSIMD
pkgname=python-simsimd
pkgver=6.0.3
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
sha512sums=('cc12d00527792cf3e1c3d3cce955f6549eff72db1b7861275448292887c33a09c64963f5befb3de829ccbcb38f072afe105ca39599fd69dbfef0e9bb92b5411a')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
