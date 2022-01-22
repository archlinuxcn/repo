# Maintainer: Jose Riha <jose1711 gmail com>

pkgname=python-m3u8
pkgver=1.0.0
pkgrel=1
pkgdesc="Python m3u8 parser"
url="https://github.com/globocom/m3u8"
depends=('python' 'python-iso8601')
makedepends=('python-setuptools')
license=('MIT')
arch=('any')
source=("https://github.com/globocom/m3u8/archive/${pkgver}.tar.gz")
md5sums=('7c50506642bd1efbd6b7799212853794')

build() {
  cd $srcdir/m3u8-${pkgver}
  python setup.py build
}

package() {
  cd $srcdir/m3u8-${pkgver}
  python setup.py install --root="$pkgdir" --optimize=1 
}
