# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchmetrics
_pkgname=torchmetrics
pkgver=0.6.1
pkgrel=1
pkgdesc='Machine learning metrics for distributed, scalable PyTorch applications'
arch=('any')
url='https://github.com/PyTorchLightning/metrics'
license=('Apache')
depends=(
  python-numpy
  python-pytorch
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/PyTorchLightning/metrics/releases/download/v${pkgver}/torchmetrics-${pkgver}.tar.gz"
)
sha512sums=('2eac873c2646dce9c7a50003e44c715acecb49fd0068d056d147e910f5ba1dd150123266eb9f805e77465930a80e0d363d6a6da378e043b15a522efff0a4a358')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
