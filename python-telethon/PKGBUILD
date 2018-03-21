_pkgname=Telethon
pkgname=python-telethon
pkgver=0.18.1.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/53/84/24725a244910372dc8149fe660947815363471662254dc294d79f5112975/Telethon-0.18.1.1.tar.gz')
md5sums=('cafb4aab57192d9e2d6e24cc60ff9aa2')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
