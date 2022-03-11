# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.18.75
pkgrel=1
pkgdesc='Tools for medical image processing in deep learning and PyTorch'
arch=('any')
url='https://github.com/fepegar/torchio'
license=('MIT')
depends=(
  python-click
  python-deprecated
  python-humanize
  python-nibabel
  python-numpy
  python-pytorch
  python-scipy
  python-simpleitk
  python-torchvision
  python-tqdm
)
makedepends=(
  python-setuptools
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/fepegar/torchio/archive/v${pkgver}.tar.gz")
sha512sums=('26ac27b4ba6ffb1fd3eb74cad1aa4a494192788c6692f8d3e2bb07d43d6d3fbbaff3086900f4fa2b95222f4ed6ecfe6a26b45f9b688a9144f3597e5b9fe07b5d')

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
