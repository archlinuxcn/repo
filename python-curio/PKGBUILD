_pkgname=curio
pkgname=python-curio
pkgver=0.4
pkgrel=1
pkgdesc="Curio - Concurrent I/O"
arch=('any')
url="https://github.com/dabeaz/curio"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/07/f8/6eb3a8f99e52cc8d95e196383755e76e2636870a57546c841658855940ca/curio-0.4.tar.gz')
md5sums=('f769a76dc394480fa7731c50f5169f39')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
