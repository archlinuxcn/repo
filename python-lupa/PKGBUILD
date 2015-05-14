_pkgname=lupa
pkgname=python-$_pkgname
pkgver=1.1
pkgrel=1
pkgdesc="Python wrapper around Lua and LuaJIT"
arch=('any')
url="https://github.com/scoder/lupa"
license=('MIT')
depends=('python' 'luajit' 'python-setuptools')
source=('https://pypi.python.org/packages/source/l/lupa/lupa-1.1.tar.gz')
md5sums=('ff5907391441222d981355676ae6f093')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
