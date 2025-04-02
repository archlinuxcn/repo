# Maintainer: Andrew O'Neill <andrew at haunted dot sh>

_pyname=circuitbreaker
pkgname=python-${_pyname}
pkgver=2.1.3
pkgrel=1
pkgdesc='Python implementation of the Circuit Breaker pattern'
arch=('x86_64')
url="https://github.com/fabfuel/${_pyname}"
license=('BSD-3-Clause')
makedepends=('python-setuptools')
depends=('python')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('0a89578d626a04e39e58c9ac28f181076ac8a88d71a4eca37b0f7a1bf7bf6755')

build() {
  cd "${_pyname}-${pkgver}"

  python setup.py build
}

package() {
  cd "${_pyname}-$pkgver"

  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE.rst "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
