_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/8e/57/ca8020c000ee07f413e2682d370a2d06e2e073548ef8abc91e16afd9d2ae/Telethon-0.17.2.tar.gz')
md5sums=('469b7601d3c373d60f673df5e5398fcb')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
