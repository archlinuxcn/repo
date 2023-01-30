# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=girder-client
pkgname=python-girder-client
pkgver=3.1.16
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
sha512sums=('8f14ec1e7100a80f028ecdcd525420c8ffcf4459c90e629397fda8d5a7e8cb01b156a37c11270bf1e5ca326eb8eab50196ffaef99989420fe8c225b8691c5fd7')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
