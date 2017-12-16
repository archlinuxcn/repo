_pkgname=lupa
pkgname=python-lupa
pkgver=1.6
pkgrel=1
pkgdesc="Python wrapper around Lua and LuaJIT"
arch=('i686' 'x86_64')
url="https://github.com/scoder/lupa"
license=('MIT')
depends=('python' 'luajit' 'python-setuptools')
source=('https://pypi.python.org/packages/fa/a5/20e320701292364fa6d1f99a76ae75119d31ee2c8f168637cef8ffc5a977/lupa-1.6.tar.gz')
md5sums=('069f88444d8c5d3264adde3a8c90d912')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
