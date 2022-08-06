# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=functorch
pkgname=python-functorch
pkgver=0.2.1
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
sha512sums=('0dacd5bbf944f4b4f0434952b2f0460bfd4683153c6b4a80a8d5385a186b92cb1568418e92e4a32bf6fbb1c785d097ba7eca231db671a585a5ed60295881b44c')

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
