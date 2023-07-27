# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=numpymaxflow
pkgname=python-numpymaxflow
pkgver=0.0.5
pkgrel=1
pkgdesc='Numpy-based implementation of Max-flow/Min-cut (graphcut) for 2D/3D data'
arch=('x86_64')
url='https://github.com/masadcv/numpymaxflow'
license=('BSD')
depends=(
  python-numpy
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/masadcv/numpymaxflow/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('b7bc515bfdf17dd4e376799030722c7e33a8515a2d4590ff388630c855b806025d0584962099e88c4252b5389715da835d7598ca1a0e29d3bd51ac9dc8606c4c')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation -x
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
