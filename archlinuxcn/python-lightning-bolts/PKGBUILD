# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-lightning-bolts
_pkgname=lightning-bolts
pkgver=0.4.0
pkgrel=1
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
sha512sums=('bd0524ea4e1b32c2d6e71f40328e77be8a64c3bb215dd1e43bfc8e12915e735b3ae421cda06099f5c324f991dfb5e0999d521e017ea6ec1b8f5ab2c10efbc7aa')

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
