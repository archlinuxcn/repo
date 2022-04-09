# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=functorch
pkgname=python-functorch
pkgver=0.1.0
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
sha512sums=('d41d17f9f2d45ca3e217a88f236fa6f43a60ca3f4635bbfcadcfb0dd82feafe557004d675f45f92737f4c0f0386d490a8110af4cd961e6d76ce99b8979e76dfd')

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
