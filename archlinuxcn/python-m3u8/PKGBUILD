# Maintainer: Jose Riha <jose1711 gmail com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>

_base=m3u8
pkgname=python-${_base}
pkgdesc="Python m3u8 parser"
pkgver=3.4.0
pkgrel=1
arch=(any)
url="https://github.com/globocom/${_base}"
license=(MIT)
depends=(python-iso8601)
makedepends=(python-setuptools)
checkdepends=(python-pytest python-bottle)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('6c8d1eb0e352b21844dab539cde5337bb6c048b10b9e412ec9e984cdc9465f24972002c1d75e024d0f3b19d4eb24298ddfa6dd86a43d57284281420b4aa2c120')

build() {
  cd ${_base}-${pkgver}
  python setup.py build
}

check() {
  cd ${_base}-${pkgver}
  python -m pytest tests -k 'not load_should_create_object_from_uri and not load_should_remember_redirect and not load_should_create_object_from_uri_with_relative_segments'
}

package() {
  cd ${_base}-${pkgver}
  python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
