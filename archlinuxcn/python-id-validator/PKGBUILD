# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=id-validator.py
pkgname=python-id-validator
pkgver=1.0.17
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
sha512sums=('629ed682a3fa77752f33b5df1a4f407500fa9eadc5c3bcf6251472994db784a80a8d8b61da6ef698d3d75d08a380ad85e118890879b4c74dc41e1aaf5f7ace71')

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
