# Maintainer:  Andrew O'Neill <andrew at haunted dot sh>

pkgname=python-ipaddress
_pyname=ipaddress
pkgver=1.0.23
pkgrel=1
pkgdesc='IPv4/IPv6 manipulation library'
arch=('x86_64')
url='https://github.com/phihag/ipaddress'
license=('custom:PSFL')
makedepends=('python-setuptools')
depends=('python')
source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('8cc01a7523042c3b1a01446f0318e8bbe0fc0d520ca651c986377e402a2e9b47')

build() {
  cd "${_pyname}-${pkgver}"

  python setup.py build
}

package() {
  cd "${_pyname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
