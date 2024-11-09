# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix

pkgname=python-fvs
pkgver=0.3.4
pkgrel=3
pkgdesc="File Versioning System with hash comparison, deduplication and data storage to create unlinked states that can be deleted"
arch=(any)
url="https://github.com/mirkobrombin/FVS"
license=(MIT)
depends=(python-orjson)
makedepends=(python-setuptools)
provides=(fvs)
conflicts=(fvs)
replaces=(vfs)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/mirkobrombin/FVS/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('c57bcda81cd7500bc54b8f93c81405cccbc4c54b794209f8316ae27f43372696')

build() {
  cd "FVS-${pkgver}"
  python setup.py build
}

package() {
  cd "FVS-${pkgver}"
  python setup.py install --skip-build --optimize=1 --prefix=/usr --root="${pkgdir}"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
