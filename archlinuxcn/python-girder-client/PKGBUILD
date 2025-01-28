# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=girder-client
_name=girder_client
pkgname=python-girder-client
pkgver=3.2.8
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
sha512sums=('7f5d7710199a8cf9073b341f37915e0776e026e9e76c1a8e8e28b0927a9a06e634b879001a1a89787da999b0abd9dd62ec045a9d44899eb4082d92f2bc1cadf6')

build() {
  cd "${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
