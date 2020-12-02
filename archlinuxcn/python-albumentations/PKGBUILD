# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albumentations
pkgname=python-albumentations
pkgver=0.5.2
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
sha512sums=('e4a03b89f18817e622f0af72583d82be4b145384ff5f3b8c346497c484be1209b38af54202d098024162d11a00c13956afab2102c38ec6536470f660b84314b1')

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
