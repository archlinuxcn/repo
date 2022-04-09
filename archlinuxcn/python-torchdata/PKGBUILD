# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=data
pkgname=python-torchdata
pkgver=0.3.0
pkgrel=1
pkgdesc='A PyTorch repo for data loading and utilities to be shared by the PyTorch domain libraries'
arch=('any')
url='https://github.com/pytorch/data'
license=('BSD')
depends=(
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
sha512sums=('201ba2ee2b9c227b9a3a61eee317a2e84f5957b8aa8a6d00cf48d4b055f6bc2332cb5094282f56399969e74dde95afda3f652a283ce41c3261a129b82e88df49')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
