# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=girder-client
_name=girder_client
pkgname=python-girder-client
pkgver=5.0.2
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
sha512sums=('e085b9332063ce0dee85fbad534d33ad987e89a05f4f8b345793450b6011f4b458a85bfa09e9551af657e5eee1170dab3dc41f4479ff45cae428f81677a0323e')

build() {
  cd "${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
