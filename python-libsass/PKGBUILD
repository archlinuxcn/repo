_pkgname=libsass
pkgname=python-libsass
pkgver=0.13.5
pkgrel=1
pkgdesc="SASS for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="http://hongminhee.org/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/02/68/a34fe46508b243a59e33020ea5b18b7b4bedb438095176f9a5060913d1cb/libsass-0.13.5.tar.gz')
md5sums=('a400dc2db9c252483b22a6c13dbb7955')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
