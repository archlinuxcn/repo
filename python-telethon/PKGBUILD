_pkgname=Telethon
pkgname=python-telethon
pkgver=0.15.4.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/bf/cb/4657e16bb44e98ed87c4ed18ce26725edaee1b533b314e6e8cbb0551efa2/Telethon-0.15.4.3.tar.gz')
md5sums=('e9e30925591aeb9949cd1cb615d2d062')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
