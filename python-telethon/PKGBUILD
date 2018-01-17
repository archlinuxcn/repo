_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.1.4
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/1a/e5/3c13251e01a7bccdbf7fad1eeab2c2a016d642bfaaa1d733fe840ac1ac1e/Telethon-0.16.1.4.tar.gz')
md5sums=('85290f83ab866e62b088549071cf76df')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
