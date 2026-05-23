# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=girder-client
_name=girder_client
pkgname=python-girder-client
pkgver=5.0.8
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
sha512sums=('e45c0885b4d6e690077adfe76ac22f4a79ce5634741a219e3fe5ddf1831dee15083ee38739f66fac33be784aed4a268e6994d7ff8ac9293376c7600204ec1674')

build() {
  cd "${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
