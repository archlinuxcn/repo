# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=girder-client
_name=girder_client
pkgname=python-girder-client
pkgver=5.0.13
pkgrel=1
pkgdesc='Python client for interacting with Girder servers'
arch=('any')
url='https://pypi.org/project/girder-client'
license=('Apache-2.0')
depends=(
  python-click
  python-diskcache
  python-requests
  python-requests-toolbelt
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-setuptools-scm
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_name}-${pkgver}.tar.gz")
sha512sums=('c7ff0b7d981e13c03039436ad5ae45b90526d5f8141a6a72f28efc01c1040b4329b0a00f1a96c2cbc5d3263bd3793380d75576300040ca7a09236f2bcd23dab0')

build() {
  cd "${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
