# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-lightning-bolts
_pkgname=lightning-bolts
pkgver=0.5.0
pkgrel=3
pkgdesc='Toolbox of models, callbacks, and datasets for AI/ML researchers'
arch=('any')
url='https://github.com/Lightning-AI/lightning-bolts'
license=('Apache')
depends=(
  python-pytorch
  python-pytorch-lightning
  python-torchmetrics
)
makedepends=(
  python-build
  python-installer
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Lightning-AI/lightning-bolts/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('cf54f5ee436b226053ed94596a53da7d82f87c990142af968dfab2da3434fceb1e45c97ecedf518fee38a9e1890204572a31c48653ebfdf5078e7c57447c7bd5')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  rm -rf "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/tests"
}
# vim:set ts=2 sw=2 et:
