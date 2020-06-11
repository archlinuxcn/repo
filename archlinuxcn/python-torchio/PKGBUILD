# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.16.25
pkgrel=1
pkgdesc='Tools for medical image processing in deep learning and PyTorch'
arch=(any)
url='https://github.com/fepegar/torchio'
license=(MIT)
depends=(
  'python-click'
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
  'python-deprecated'
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/fepegar/torchio/archive/v${pkgver}.tar.gz")
sha512sums=('ff6b16b1d5d64b1bfeeab54dd9ab780975814f4736676017d245e3228cedd63016c6034e0b9009fdca2d8cb5929abeb99a93355bdba5a220ba86cbbc7e49d371')

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
