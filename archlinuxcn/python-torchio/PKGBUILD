# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.18.82
pkgrel=1
pkgdesc='Tools for medical image processing in deep learning and PyTorch'
arch=('any')
url='https://github.com/fepegar/torchio'
license=('MIT')
depends=(
  python-click
  python-deprecated
  python-humanize
  python-matplotlib
  python-nibabel
  python-numpy
  python-pytorch
  python-scipy
  python-simpleitk
  python-torchvision
  python-tqdm
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/fepegar/torchio/archive/v${pkgver}.tar.gz")
sha512sums=('12d2a18f7edff32b0edfa2f416ee616c594ba2a0c1252f178b6eec422a2aa0a258124e4f898efe8f53e2c9adba4d55a356e92b9bcaf878ed30ff32383db2ee2f')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
