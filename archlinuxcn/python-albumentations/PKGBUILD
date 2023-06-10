# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albumentations
pkgname=python-albumentations
pkgver=1.3.1
pkgrel=1
pkgdesc='Fast image augmentation library and easy to use wrapper around other libraries'
arch=('any')
url='https://github.com/albumentations-team/albumentations'
license=('MIT')
depends=(
  python-imgaug
  python-numpy
  python-opencv
  python-pillow
  python-qudida
  python-tqdm
  python-yaml
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/albumentations-team/albumentations/archive/${pkgver}.tar.gz")
sha512sums=('e93e9ea9ca8b76731a528894e460ee2efeffa3be10c3845a84d4ac55da739472639a7e95024181006112efe1a1ea8d8044db4d3ba2b5dbf80d655a8cbaa218cd')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
