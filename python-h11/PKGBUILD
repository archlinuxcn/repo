_pkgname=h11
pkgname=python-h11
pkgver=0.7.0
pkgrel=1
pkgdesc="A pure-Python, bring-your-own-I/O implementation of HTTP/1.1"
arch=('any')
url="https://github.com/njsmith/h11"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/50/13/954a4bd263857262a0b07155b47f5494a02b97984a5bcc6263bf89f12586/h11-0.7.0.zip')
md5sums=('e411d454aa515cf9cbd43cd12999b3d2')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
