# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-imantics
_pkgname=imantics
pkgver=0.1.12
pkgrel=4
pkgdesc='Reactive python package for managing, creating and visualizing different deep-learning image annotation formats'
arch=('any')
url='https://github.com/jsbroks/imantics'
license=('MIT')
depends=(
  python-opencv
  python-lxml
  python-xmljson
  python-numpy
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/jsbroks/imantics/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('7aeec091672479bd5f7b1162cec2a8e48581ae06ebda9ea37a148b3ae09afa58dc0cd662030c4635e2b481e94e8a4568241d2e60cb28e1a7e24fcf4253f24eec')

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
