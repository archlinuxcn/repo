# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albumentations
pkgname=python-albumentations
pkgver=1.2.1
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
sha512sums=('4e2ce89e3842fd626749cbfaffd69e15eb13c8f398ff07a090d8e8762c9ee0d672cc6e3ff9504b75273a34952938bb5dc2b62763474a178da74e4aabf531a617')

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
