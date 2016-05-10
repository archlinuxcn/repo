_pkgname=curio
pkgname=python-curio
pkgver=0.2
pkgrel=1
pkgdesc="Curio - Concurrent I/O"
arch=('any')
url="https://github.com/dabeaz/curio"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/f1/fe/bc964152f5a5fa954857d73d4794878aef6a05f12d54f3baa79cf3ff4fbf/curio-0.2.tar.gz')
md5sums=('1147705031b0a4fce950599fc07c8625')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
