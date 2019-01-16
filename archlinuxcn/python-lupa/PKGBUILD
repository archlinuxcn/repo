_pkgname=lupa
pkgname=python-lupa
pkgver=1.7
pkgrel=1
pkgdesc="Python wrapper around Lua and LuaJIT"
arch=('i686' 'x86_64')
url="https://github.com/scoder/lupa"
license=('MIT')
depends=('python' 'luajit' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/f2/b2/8295ebabb417173eaae05adc63353e4da3eb8909e1b636b17ff9f8e1cdce/lupa-1.7.tar.gz')
md5sums=('3b126fc77d1dce4faa4d1c02d3de01cb')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
