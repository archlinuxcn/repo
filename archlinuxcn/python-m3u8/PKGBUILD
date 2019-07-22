# Maintainer: Jose Riha <jose1711 gmail com>

pkgname=python-m3u8
pkgver=0.3.10
pkgrel=1
pkgdesc="Python m3u8 parser"
url="https://github.com/globocom/m3u8"
depends=('python' 'python-iso8601')
makedepends=('python-setuptools')
license=('MIT')
arch=('any')
source=("https://files.pythonhosted.org/packages/08/d1/3de706f032da975525f9b78d1858b085155a9fe6669dd5dcebe6e7cacc4e/m3u8-${pkgver}.tar.gz")
md5sums=('7e1f915779e35e564bd1afe1aa2fe3b0')

build() {
    cd $srcdir/m3u8-${pkgver}
    python setup.py build
}

package() {
    cd $srcdir/m3u8-${pkgver}
    python setup.py install --root="$pkgdir" --optimize=1 
}
