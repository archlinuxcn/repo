# Maintainer: Hilton Medeiros <medeiros.hilton@gmail.com>

pkgname=python2-bjoern
_pkgname=bjoern
pkgver=1.4.2
pkgrel=1
pkgdesc="A screamingly fast, ultra-lightweight WSGI server for Python, written in C."
arch=('i686' 'x86_64')
url="https://github.com/jonashaag/bjoern"
license=('BSD')
depends=('libev' 'python2')
makedepends=('python2-setuptools')
source=("http://pypi.python.org/packages/source/b/$_pkgname/$_pkgname-$pkgver.tar.gz")
md5sums=('bd0b1d97a187fd438a8959dfb312683d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python2 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python2 setup.py install --skip-build --root="$pkgdir" -O1
  install -D LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
} 
