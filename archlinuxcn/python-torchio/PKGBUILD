# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=1.0.2
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
sha512sums=('399ff182d0b2745cfb2434f441ced0c608d154e9e4c4c4d9d93e247e66f974c2a278142d910560221d198482fdea63c6d284e3b376e70ffbd88f53826c0858cb')

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
