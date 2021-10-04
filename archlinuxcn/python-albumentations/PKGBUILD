# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albumentations
pkgname=python-albumentations
pkgver=1.1.0
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
sha512sums=('9c6188e36b8c6761e16cc579a9cba317cb7fdf8262a7671ef5c90d72633b3c5dfcdfa8300514d31d34cdc8ced69fe7709467b7bdf8e0572a8cd0fe3baec6d36a')

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
