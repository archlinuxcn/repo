_pkgname=libsass
pkgname=python-libsass
pkgver=0.15.1
pkgrel=1
pkgdesc="Sass for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://files.pythonhosted.org/packages/76/04/ecad53596a118fd77c9d8d00fcb81e4ea0ae0829d2bf87216c80948ed88e/libsass-0.15.1.tar.gz')
md5sums=('15bde5b9e3bc42a7b471576fc0fe897f')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
