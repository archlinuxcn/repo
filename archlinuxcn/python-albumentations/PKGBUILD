# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albumentations
pkgname=python-albumentations
pkgver=1.0.1
pkgrel=1
pkgdesc='Fast image augmentation library and easy to use wrapper around other libraries'
arch=(any)
url='https://github.com/albumentations-team/albumentations'
license=('MIT')
depends=(
  opencv
  python-imgaug
  python-numpy
  python-pillow
  python-tqdm
  python-yaml
)
makedepends=(python-setuptools)
checkdepends=(
  hdf5
  python-pytest
  python-pytorch
  python-torchvision
  qt5-base
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/albumentations-team/albumentations/archive/${pkgver}.tar.gz")
sha512sums=('0406b327b4aa3efbf301e337242aae37b05b566412c9173185ea2e97983a82102cd6549292dede6966109b5477986b4cd516bd8538f454c52b76d0b25f0c2b2a')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib.linux-${CARCH}-$(get_pyver)" pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
