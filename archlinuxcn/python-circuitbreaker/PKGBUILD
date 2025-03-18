# Maintainer: Andrew O'Neill <andrew at haunted dot sh>

_pyname=circuitbreaker
pkgname=python-${_pyname}
pkgver=2.1.0
pkgrel=1
pkgdesc='Python implementation of the Circuit Breaker pattern'
arch=('x86_64')
url="https://github.com/fabfuel/${_pyname}"
license=('BSD-3-Clause')
makedepends=('python-setuptools')
depends=('python')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('5eb2ba29c778d622a3d7aacd964f15e171d51221072bae7db06b376070591eb8')

build() {
  cd "${_pyname}-${pkgver}"

  python setup.py build
}

package() {
  cd "${_pyname}-$pkgver"

  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE.rst "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
