# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=python-google
pkgver=3.0.0
pkgrel=2
pkgdesc='Google search from Python'
arch=('any')
url='https://github.com/MarioVilas/googlesearch'
license=('BSD')
depends=(python-beautifulsoup4)
makedepends=(python-setuptools)
source=("$pkgname-$pkgver.tar.gz::https://github.com/MarioVilas/googlesearch/archive/v$pkgver.tar.gz")
sha256sums=('9fd814876322b84f7f73499f3bd96b4da7533904e7f00c6dea2e262a467889d1')

_pkgname=googlesearch

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
