# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=functorch
pkgname=python-functorch
pkgver=1.13.0
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
sha512sums=('81ece7ea1694ccecdb150cf57719c8e5f96205ca70900b1ad44b15035a61547831586d6b827975b99acf33b77d881876573305ecf435cc884cb00fef4840cfc3')

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
