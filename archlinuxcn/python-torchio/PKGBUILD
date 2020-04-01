# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchio
_pkgname=torchio
pkgver=0.14.0
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
sha512sums=('2d7f6a066eed89bb3ecfb7fe33ec6b9532d38d6d4631f720cca3b4deb97874d30d7ee43de36fa3e294a616567eca68836476e207b49ef6e02ccb331b882d3f93')

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
