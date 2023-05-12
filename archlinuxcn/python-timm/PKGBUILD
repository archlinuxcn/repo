# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=timm
pkgname=python-timm
pkgver=0.9.1
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
sha512sums=('545085f699e9d15037aa2520cb04695b5c1381aa0a7895d0bc1e7c60c47be2835c293d4f8ec4e684f06c29491353bf60bf552991f4fbc07efc72010cb98ec8c3')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
