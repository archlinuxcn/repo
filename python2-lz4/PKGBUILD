# Maintainer: Vladimir Tsanev <tsachev@gmail.com>
pkgname=python2-lz4
pkgver=0.7.0
pkgrel=1
pkgdesc="LZ4 Bindings for Python"
arch=('any')
url="https://github.com/steeve/python-lz4"
license=('BSD')
makedepends=('python2-distribute')
depends=('python2')
source=(http://pypi.python.org/packages/source/l/lz4/lz4-$pkgver.tar.gz)
md5sums=('e32842a49d5254f6918567197a704492')

package() {
  cd $srcdir/lz4-$pkgver
  python2 setup.py install --root=$pkgdir || return 1
} 
