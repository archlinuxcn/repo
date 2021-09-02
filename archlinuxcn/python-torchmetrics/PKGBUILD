# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchmetrics
_pkgname=torchmetrics
pkgver=0.5.1
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
sha512sums=('52dba311c0ce06849035c7a39bdf48131af44f5420133259c7fefbd29bbceabacc70abd51d961c2e45bf8dc5741522cec73aec3c6c605c0fd2c20522f517c224')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
