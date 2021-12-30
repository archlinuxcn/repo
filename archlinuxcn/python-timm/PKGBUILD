# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=timm
pkgname=python-timm
pkgver=0.4.12
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
sha512sums=('ab52b2ace07b9caf8e8f42cd3c68c4bdca12ec6ee7886324d55cf31cc43faa50c0839f3bf589fceaaf162a738d554f471099a77b7c34d0ce20cd355f1744ab83')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
