_pkgname=lupa
pkgname=python-lupa
pkgver=1.4
pkgrel=1
pkgdesc="Python wrapper around Lua and LuaJIT"
arch=('i686' 'x86_64')
url="https://github.com/scoder/lupa"
license=('MIT')
depends=('python' 'luajit' 'python-setuptools')
source=('https://pypi.python.org/packages/a4/36/9a8d7cda4fda8c6cc3fd3198c1a98cdfefdb6fe1db5b88f6784d09cd9d86/lupa-1.4.tar.gz')
md5sums=('eece9f76b7b7af6cb494314835ada225')

export LANG=en_US.UTF-8

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
