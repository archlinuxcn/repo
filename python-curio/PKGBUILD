_pkgname=curio
pkgname=python-curio
pkgver=0.6
pkgrel=1
pkgdesc="Curio - Concurrent I/O"
arch=('any')
url="https://github.com/dabeaz/curio"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/ba/dd/195ec56561211e7a53e31ae45dcb143c7bcc5d8c776c7efc6f1a46d9c77d/curio-0.6.tar.gz')
md5sums=('3acba1233f93d7c34de8be8cb0d0de29')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
