_pkgname=libsass
pkgname=python-libsass
pkgver=0.13.1
pkgrel=1
pkgdesc="SASS for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="http://hongminhee.org/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/fa/73/83ae26e2778b6629d834b365e2594fb00817eb54cf0703c26f9e0785b71d/libsass-0.13.1.tar.gz')
md5sums=('fe94d537647e1bb316d40ab66dfe3223')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
