_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17.1.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/a3/61/f74ae265be5a5239acc9ae8038bc00184b0a2e4a3ca8b524fbf245adfa4d/Telethon-0.17.1.2.tar.gz')
md5sums=('231506cdab40e9a90dc547c68a575e38')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
