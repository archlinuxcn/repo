_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17.4.5
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/7d/00/5422a924129066394fd7f6e64a5816cd2307d78d00d7feca4c4c286ce8b5/Telethon-0.17.4.5.tar.gz')
md5sums=('c9847c43f7bfe83a7ade224c274ba6b1')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
