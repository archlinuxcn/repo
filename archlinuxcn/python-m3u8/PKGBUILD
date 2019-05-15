# Maintainer: Jose Riha <jose1711 gmail com>

pkgname=python-m3u8
pkgver=0.3.8
pkgrel=2
pkgdesc="Python m3u8 parser"
url="https://github.com/globocom/m3u8"
depends=('python' 'python-iso8601')
makedepends=('python-setuptools')
license=('MIT')
arch=('any')
source=("https://files.pythonhosted.org/packages/ba/73/45b2700bfb3e31bdc985a4c1afb8e16e85137c2b980faa3ee2711074e650/m3u8-${pkgver}.tar.gz")
md5sums=('a04e59871d0ce02327b741b539aa6ac9')

build() {
    cd $srcdir/m3u8-${pkgver}
    python setup.py build
}

package() {
    cd $srcdir/m3u8-${pkgver}
    python setup.py install --root="$pkgdir" --optimize=1 
}
