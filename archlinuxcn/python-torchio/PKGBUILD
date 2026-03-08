# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.21.4
pkgrel=1
pkgdesc='Tools for medical image processing in deep learning and PyTorch'
arch=('any')
url='https://github.com/TorchIO-project/torchio'
license=('MIT')
depends=(
  python-click
  python-deprecated
  python-humanize
  python-matplotlib
  python-nibabel
  python-numpy
  python-pytorch
  python-rich
  python-scipy
  python-simpleitk
  python-torchvision
  python-tqdm
  python-typer
)
makedepends=(
  python-build
  python-uv-build
  python-installer
  python-wheel
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/fepegar/torchio/archive/v${pkgver}.tar.gz")
sha512sums=('02b234d39968efd6ad1c14439147258be1c96ec8f53f1c865ecff3c98d4bc2cf78b1473c5c3982a2f6cf5e65af1fde5e9787dd5bb8a71fd7c2579217678f04ea')

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
