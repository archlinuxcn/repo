# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=id-validator.py
pkgname=python-id-validator
pkgver=1.0.15
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
sha512sums=('e12928a61ca71418843bbfad8be9732db8a082e5e74527c00e90b28cc62f291402cf24e5d1c7e9fcd8163934c409f71edf49a8f82117c70a040b65a16b1226bb')

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
