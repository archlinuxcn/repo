# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.19.3
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
sha512sums=('0fe785afa5b0a892a70021e3b8215533cecb4865931111b221a6fabfda6889a4c619bd19224bfa5f1267852efb52d67e293c5cacf527ff0931b6df8458a99007')

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
