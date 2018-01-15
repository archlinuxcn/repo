_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.1.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/07/35/feb7877612fa5e874bf3102ea86e0058a45d41e013fdf3e0a0ab166e3c6d/Telethon-0.16.1.2.tar.gz')
md5sums=('f4104a2e84681cdc511f4e70fddea78f')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
