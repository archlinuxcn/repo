_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.0.9
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/5c/32/aef9de5046a918f006d1fb823347a37705230f34f21033bf89074fdb47c4/Telethon-0.16.0.9.tar.gz')
md5sums=('9541f2a867f62f90856cd58d3dc2a1e6')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
