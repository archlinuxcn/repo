_pkgname=lupa
pkgname=python-lupa
pkgver=1.2
pkgrel=1
pkgdesc="Python wrapper around Lua and LuaJIT"
arch=('i686' 'x86_64')
url="https://github.com/scoder/lupa"
license=('MIT')
depends=('python' 'luajit' 'python-setuptools')
source=('https://pypi.python.org/packages/source/l/lupa/lupa-1.2.tar.gz')
md5sums=('f312b90674ff18883ddead01c0d512ef')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
