# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=data
pkgname=python-torchdata
pkgver=0.4.0
pkgrel=1
pkgdesc='A PyTorch repo for data loading and utilities to be shared by the PyTorch domain libraries'
arch=('any')
url='https://github.com/pytorch/data'
license=('BSD')
depends=(
  python-portalocker
  python-pytorch
  python-requests
  python-urllib3
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/pytorch/data/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('b33c21b04efc5c78f3d25c04f499e40b542f61c486dddad43ef605cf958089087a8612a609c4946ca43bdf408172d9a96130c008fd7b29ccf2e34562785f1bc7')

build() {
  cd "${_pkgname}-${pkgver}"
  USE_SYSTEM_LIBS=ON \
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
