_pkgname=butterfly
pkgname=butterfly
pkgver=3.0.0
pkgrel=1
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="http://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=('https://pypi.python.org/packages/e6/f3/0de160fd27d6eedfdebae8e73cd35d702fa6324bb9a4d320c308c13f81df/butterfly-3.0.0.tar.gz')
md5sums=('0ad4979adad02e05ae5535e091c22998')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
