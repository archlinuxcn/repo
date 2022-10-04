# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=timm
pkgname=python-timm
pkgver=0.6.11
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
sha512sums=('c0ada9c633de375f3a160c1fe211baef839aa533bdc3dc102d66b56277b49e97133b8b5b33512f3b150d3f8dd290d3138de977778669553b95caa9c6296ca79b')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
