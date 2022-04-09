# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.18.76
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
sha512sums=('5279fcdee7e739b3d712c8ecb9eeb9e730aafc52a861f4561684d1b9421ccdcd04d9d4674d45a3e1390a32494aefac03ba1c7a8f20cb624595efb1337911fde7')

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
