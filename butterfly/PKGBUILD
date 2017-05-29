_pkgname=butterfly
pkgname=butterfly
pkgver=3.1.5
pkgrel=1
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="https://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=('https://pypi.python.org/packages/21/79/9a9337228906388def9eaae5fd25e308cd6e443da4f332ea86216b893170/butterfly-3.1.5.tar.gz')
md5sums=('a0c96c5f4d1b287b20baca4f34b3179f')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
