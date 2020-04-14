# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albumentations
pkgname=python-albumentations
pkgver=0.4.0
pkgrel=2
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
sha512sums=('167996873015dae2bee21f02c75d7e365353a1ada9b4da3c3c574d2d66e779d72dbe831bd576b6fb69cab773873cc36bdc0b15d0ba3acb5585176893b2299244')

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
