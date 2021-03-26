# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=id-validator.py
pkgname=python-id-validator
pkgver=1.0.16
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
sha512sums=('50748783cb7c5165911a461841f8a6142ab417d930e61fa48ecbe8d8a578a47e5b86919f607c9615c5fff6bf43d39c8ccb1fbb988cbea9e0784e12ec86dd4b0b')

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
