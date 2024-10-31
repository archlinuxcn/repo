# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=numpymaxflow
pkgname=python-numpymaxflow
pkgver=0.0.7
pkgrel=1
pkgdesc='Numpy-based implementation of Max-flow/Min-cut (graphcut) for 2D/3D data'
arch=('x86_64')
url='https://github.com/masadcv/numpymaxflow'
license=('BSD-3-Clause')
depends=(
  gcc-libs
  glibc
  python-numpy
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/masadcv/numpymaxflow/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('eeb6afca38053be4aba9597e96b199d62e84e1caebcb0ebde71becc7f6c37b22ec5703ce7c822828b4217113dcbf14c024a8dd8436707795e98bd1545d0fe510')

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
