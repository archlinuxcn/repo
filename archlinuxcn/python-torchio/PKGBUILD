# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.18.6
pkgrel=1
pkgdesc='Tools for medical image processing in deep learning and PyTorch'
arch=(any)
url='https://github.com/fepegar/torchio'
license=(MIT)
depends=(
  'python-click'
  'python-deprecated'
  'python-humanize'
  'python-nibabel'
  'python-numpy'
  'python-pytorch'
  'python-scipy'
  'python-simpleitk'
  'python-torchvision'
  'python-tqdm'
)
makedepends=(
  'python-setuptools'
)
checkdepends=(
  'python-pytest'    
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/fepegar/torchio/archive/v${pkgver}.tar.gz")
sha512sums=('338c96f5019886748cc41493f1457142a28b87de1cf5c378be36bd197264d288d3b43a43d3482c2a01af7d1d0c88e74d6c47ebb8230c8207d90b8027d9b76d24')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  pytest -v .
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
