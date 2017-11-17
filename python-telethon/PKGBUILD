_pkgname=Telethon
pkgname=python-telethon
pkgver=0.15.5
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/1d/c6/95daf9a5805829fd132e57ca597611655f09b41ebcddfb852d2b1387b6b0/Telethon-0.15.5.tar.gz')
md5sums=('17f583f8811b3427d3abfdbbf8452564')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
