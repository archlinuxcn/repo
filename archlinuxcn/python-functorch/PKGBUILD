# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=functorch
pkgname=python-functorch
pkgver=2.0.0
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
sha512sums=('0258d2ba81a930b999b77151f75cdd3b6fca3af95eef5123ace74468f0c00f21feb1e2f41fc5ea79a9159e5d2adb9c3a87eae2ef77bfb5808653d6b01a7b8f36')

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
