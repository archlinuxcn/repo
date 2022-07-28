# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=timm
pkgname=python-timm
pkgver=0.6.7
pkgrel=1
pkgdesc='PyTorch Image Models'
arch=('any')
url='https://pypi.org/project/timm/'
license=('Apache')
depends=(
  python-pytorch
  python-torchvision
  python-yaml
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-$pkgver.tar.gz")
sha512sums=('e74e39f0b3b31145ef4e90f4cb6c5bd39d77683fa0359360951a7941c019d1f4f473d8f6b8827d3f3ca81c6eb332068da50e0e5e81fbfd25a8bea3f85f66d59a')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
