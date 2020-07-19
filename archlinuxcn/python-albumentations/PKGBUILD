# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albumentations
pkgname=python-albumentations
pkgver=0.4.6
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
sha512sums=('c70b5621636f554171910ffa4bfd9e21100f5130d56ffe0e4e0a6bdc09816e492a705deb4780e40cb4b9bd919bf60f7f153a7feb2f3048e403f08d4de0f73ac8')

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
