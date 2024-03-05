# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albumentations
pkgname=python-albumentations
pkgver=1.4.1
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
sha512sums=('46ae6683c47dcaf9ec6b426bc5710551f6147fd86739c7e9129989ad730f584cd70634c31ca705f657bdac1491b3762aa50782ba5ccd6c013e029f19d45bcc5a')

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
