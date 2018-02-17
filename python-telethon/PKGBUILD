_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17.2.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/54/1f/bd50cd2836e3aa3cc055d38a5072d999a799721d915816ceeade82560eac/Telethon-0.17.2.3.tar.gz')
md5sums=('f8b1598a9ddce354c63186c9ea1cb2d8')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
