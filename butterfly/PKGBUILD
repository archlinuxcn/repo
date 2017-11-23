_pkgname=butterfly
pkgname=butterfly
pkgver=3.2.2
pkgrel=1
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="https://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=('https://pypi.python.org/packages/08/93/989926deaf636d9ae542983cf1d7c1bde082692972025f0bf34c05bef98d/butterfly-3.2.2.tar.gz')
md5sums=('3f533025518e7c7147b911320d027c60')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
