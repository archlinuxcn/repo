# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=girder-client
pkgname=python-girder-client
pkgver=3.2.0
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
sha512sums=('3ddb6dd42b0df191dc5977d238e2c0854ee1ac0dc4b090f5b7301d568d879be991246204ef901d9ca094ddeb4507bcec16deaa9d1789d8d7e9f79708970438d2')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
