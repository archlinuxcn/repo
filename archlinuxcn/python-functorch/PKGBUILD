# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=functorch
pkgname=python-functorch
pkgver=0.2.0
pkgrel=1
pkgdesc='JAX-like composable function transforms for PyTorch'
arch=('x86_64')
url='https://github.com/pytorch/functorch'
license=('BSD')
depends=(
  python-pytorch
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/pytorch/functorch/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('099c5f0205575ae960890067e8a36b2d5d8d5aebac3cbca0c530ffd339d0d8bf253ce4d6b21100bb4da78b40a24371538009e6887815ee8529557ddd1fca6613')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
