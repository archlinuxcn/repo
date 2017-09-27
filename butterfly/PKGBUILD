_pkgname=butterfly
pkgname=butterfly
pkgver=3.2.0
pkgrel=1
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="https://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=('https://pypi.python.org/packages/a4/ac/0411c45ad640050a4d3b6fa959d01d28470b4acfc4a150ca9bcd6b2b779f/butterfly-3.2.0.tar.gz')
md5sums=('e0d45e4ca24eeca7a5b2bc5eca7d35d8')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
