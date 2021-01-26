# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.18.21
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
sha512sums=('a0adfc438aa0132477fc2706345aed025f59e751b7b16ddcb517a1c3d012ad72540e0fdd2d70ba152f744e954321bbfa0177b60d61c47a085c077c6c18e683e3')

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
