# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=aioice
pkgname=python-aioice
pkgver=0.8.0
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
sha512sums=('b5b6ce07fd9e9db4b4cbe9cde4faab5372f27c918294b15e48d5645cdf4e5f2c097641a94a98d2ed9d48c361a6f6dcaf7a5579e6f46d86fa3e55a0fcadb3dcb4')

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
