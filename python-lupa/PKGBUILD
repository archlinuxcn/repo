_pkgname=lupa
pkgname=python-lupa
pkgver=1.5
pkgrel=1
pkgdesc="Python wrapper around Lua and LuaJIT"
arch=('i686' 'x86_64')
url="https://github.com/scoder/lupa"
license=('MIT')
depends=('python' 'luajit' 'python-setuptools')
source=('https://pypi.python.org/packages/8b/ee/1bb9803bbe6f06bd5dc6272cbf700f0e604906cf84a4a9ef581667e689d2/lupa-1.5.tar.gz')
md5sums=('6d05162b810863f99c44722b31592708')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
