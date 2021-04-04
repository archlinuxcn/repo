# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=id-validator.py
pkgname=python-id-validator
pkgver=1.0.18
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
sha512sums=('a8d0d3b98162f5dcb2542d08b731a9500f915e9866495e06a57fad12a16b8befa57cdb02834ed92a5b48a3e50667a00316e115447d5581551f86b4f9e2d83fa0')

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
