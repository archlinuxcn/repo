# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=girder-client
pkgname=python-girder-client
pkgver=3.2.2
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
sha512sums=('aecf49e3293c604aae1c29b1cb9e3a53e62604ff278cf601124cce22b2d0e2278c85d10e7234ed915e614bcb1794b9782496b3cc9be24dd076f0cc2129ef0195')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
