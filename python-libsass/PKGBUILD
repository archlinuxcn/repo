_pkgname=libsass
pkgname=python-libsass
pkgver=0.12.3
pkgrel=1
pkgdesc="SASS for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="http://hongminhee.org/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/77/3e/3854643362efea519450b60dec8cee6775ebf104cae4cf98f3c6d23fb3bd/libsass-0.12.3.tar.gz')
md5sums=('b2b0735a975731e1d07804fd4e7251c2')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
