_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.2.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/09/ae/3b1ac1048ed38a31db30b519201b5b78b142ce8f910f67ef776547da5a5b/Telethon-0.16.2.1.tar.gz')
md5sums=('2608bb44141bff6648a1fbaadfaadef9')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
