# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=numpymaxflow
pkgname=python-numpymaxflow
pkgver=0.0.6
pkgrel=2
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
sha512sums=('79700534b1d38d1ba66a8fe46d71fb6f15fafd3a2b8f1d319ef226ea0b38a34651529177d2ea423f8237557d04b6874a795f1ca3117c000f4f7f5ef0d8c86283')

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
