_pkgname=butterfly
pkgname=butterfly
pkgver=3.0.1
pkgrel=1
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="http://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=('https://pypi.python.org/packages/1c/7d/556845ef8d0666d1417a991fd418377397722a2b91459104647eecf0199f/butterfly-3.0.1.tar.gz')
md5sums=('a9c063eed3ae6c9b1984980a7a5d4742')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
