_pkgname=lupa
pkgname=python-lupa
pkgver=1.8
pkgrel=1
pkgdesc="Python wrapper around Lua and LuaJIT"
arch=('i686' 'x86_64')
url="https://github.com/scoder/lupa"
license=('MIT')
depends=('python' 'luajit' 'python-setuptools')
_name=${pkgname#python-}
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_pkgname}-${pkgver}.tar.gz")
md5sums=('2e717ce0a3d8958307fb4a0c2354435f')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
