# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=girder-client
pkgname=python-girder-client
pkgver=3.1.24
pkgrel=1
pkgdesc='Python client for interacting with Girder servers'
arch=('any')
url='https://pypi.org/project/girder-client'
license=('Apache')
depends=(
  python-click
  python-diskcache
  python-requests
  python-requests-toolbelt
)
makedepends=(
  python-pip
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('f8f8468ecd40b7dc284cb0b98228cdc26224a93a44c03b15423231f724dd4870c66210a2d41afdf59847df9618a401f3c242a3aefaac41029264306e3533ee4b')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
