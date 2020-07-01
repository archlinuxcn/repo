# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.17.7
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
sha512sums=('c0021cce53f2132f3bb3a401dab9a96d9a5c38a27c2b9411af27e083856eb18e2db58e648edf680159ad21d1448570a22c3737adb79207538a7b848e39908235')

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
