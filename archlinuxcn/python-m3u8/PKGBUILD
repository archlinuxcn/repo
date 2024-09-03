# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Jose Riha <jose1711 gmail com>
_base=m3u8
pkgname=python-${_base}
pkgdesc="Python m3u8 parser"
pkgver=6.0.0
pkgrel=2
arch=(any)
url="https://github.com/globocom/${_base}"
license=(MIT)
depends=(python-iso8601)
makedepends=(python-build python-installer python-setuptools python-wheel)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('83f2f77772a957671a82fa482e7bc3e95a043c077e9ba2c5372c845c4fbbd2095d5eb4069ce5ca89c968cd4d6024fdee1ee87aa43a7a82bf392439275d45e137')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
