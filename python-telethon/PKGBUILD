_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.0.6
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/31/ef/753409e7acdb8f19a9c40ad159c24b28d9a58e0b66997609201f810b2a16/Telethon-0.16.0.6.tar.gz')
md5sums=('d4ab834539e48d81ec5feafaed9e40b6')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
