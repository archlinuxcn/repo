# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-lightning-bolts
_pkgname=lightning-bolts
pkgver=0.3.4
pkgrel=2
pkgdesc='Toolbox of models, callbacks, and datasets for AI/ML researchers'
arch=('any')
url='https://github.com/PyTorchLightning/lightning-bolts'
license=('Apache')
depends=(
  python-pytorch
  python-pytorch-lightning
  python-torchmetrics
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/PyTorchLightning/lightning-bolts/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('edc4e3045b1af18905b605c3393ddd82b2107e0f31fc251f1499f20af2e317b5d4a50a9b146e70e735245c0f828a25c0da8486cbc69cdd54fa6545983fe83077')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  rm -rf "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/tests"
}
# vim:set ts=2 sw=2 et:
