# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix

pkgname=python-steamgriddb
pkgver=1.0.5
pkgrel=4
pkgdesc="Python API wrapper for SteamGridDB.com"
arch=(any)
url="https://github.com/ZebcoWeb/python-steamgriddb"
license=(MIT)
depends=(python python-requests)
makedepends=(python-setuptools)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ZebcoWeb/python-steamgriddb/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('7acb542b926ac2878040302043c8ad44aae0c3de6a9b95ed295500171119f328')

build() {
  cd "${pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${pkgname}-${pkgver}"
  python setup.py install --skip-build --optimize=1 --prefix=/usr --root="${pkgdir}"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
