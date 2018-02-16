_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17.2.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/ab/21/ca2d201767cdb9064e189b3ae094bca81846b0b21a16d7541a147b04ef64/Telethon-0.17.2.2.tar.gz')
md5sums=('9fc4cf63a5f84c9cd957d55a8d4dbd01')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
