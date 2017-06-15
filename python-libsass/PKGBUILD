_pkgname=libsass
pkgname=python-libsass
pkgver=0.13.2
pkgrel=1
pkgdesc="SASS for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="http://hongminhee.org/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/f1/db/49d9596da8fecb33125195eb84e0dd4db2769db003120bd1b4526690829a/libsass-0.13.2.tar.gz')
md5sums=('8aa0da9b4b809d2f1ec9bbd06a223047')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
