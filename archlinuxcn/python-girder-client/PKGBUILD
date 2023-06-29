# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=girder-client
pkgname=python-girder-client
pkgver=3.1.21
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
sha512sums=('d7494b23e7cf4cd6d92b9611d4858cca0254e0c4678da380cf90a7aadb06c902529f6995707c7928c69c87a61bf3f2c47f9fef80d01983946d18b620b4f3072f')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
