# Maintainer: Jose Riha <jose1711 gmail com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>

_base=m3u8
pkgname=python-${_base}
pkgdesc="Python m3u8 parser"
pkgver=3.5.0
pkgrel=1
arch=(any)
url="https://github.com/globocom/${_base}"
license=(MIT)
depends=(python-iso8601)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-bottle)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('ecc80f48311205f37213c0163ffa2c0989de4400fe39473b86267225cc7accff6aa016b1fc6dfc2e25d0479c332dcfb6244f9729798c3d1a302399913a062197')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m pytest tests -k 'not load_should_create_object_from_uri and not load_should_remember_redirect and not load_should_create_object_from_uri_with_relative_segments'
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
