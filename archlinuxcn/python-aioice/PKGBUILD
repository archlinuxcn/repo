# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=aioice
pkgname=python-aioice
pkgver=0.7.5
pkgrel=1
pkgdesc='asyncio-based Interactive Connectivity Establishment (RFC 5245)'
arch=('any')
url='https://github.com/aiortc/aioice'
license=('BSD')
depends=(
  python-dnspython
  python-netifaces
)
makedepends=(
  python-setuptools
)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/aiortc/aioice/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('b7c0a186b31b8cfc81aebf87ed9a291b393b4faf5ed49933a224849738106135c735ab2e23adc40cfa7008d586f033c19785b204a665826a49e0b42afd3c2987')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
