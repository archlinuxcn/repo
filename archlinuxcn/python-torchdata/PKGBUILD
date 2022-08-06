# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=data
pkgname=python-torchdata
pkgver=0.4.1
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
sha512sums=('1723aa052db374945c6fd73e012a0668fe8b74afce107ea65c7b65ed9acebfd8e500c3dd6223cf483ff61d90f0898aaa7492165c4fc68c2e2e0c64b29d005408')

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
