# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=id-validator.py
pkgname=python-id-validator
pkgver=1.0.14
pkgrel=1
pkgdesc='中华人民共和国居民身份证、中华人民共和国港澳居民居住证以及中华人民共和国台湾居民居住证号码验证工具'
arch=('any')
url='https://github.com/jxlwqq/id-validator.py'
license=('MIT')
makedepends=(
  python-setuptools
)
checkdepends=(
  python-pytest
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/jxlwqq/id-validator.py/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('ab08de721c8dd383c5f4767e1a836a97b4296d7dbbadb91bfc15f653fabe7866bb707dc4e9b57bdcf7571555069e15c1c47c519881091cd278829b191d7801bb')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
