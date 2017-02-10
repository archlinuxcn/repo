_pkgname=butterfly
pkgname=butterfly
pkgver=2.0.2
pkgrel=1
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="http://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=('https://pypi.python.org/packages/25/ef/01cd00716876d8612206087017e22525dd5cb171fb145ba72535204b169b/butterfly-2.0.2.tar.gz')
md5sums=('e8c5c3941f58380adeb9f6ea91c63553')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
