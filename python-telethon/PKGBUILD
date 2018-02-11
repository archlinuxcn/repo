_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17.1.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/69/ca/34dba9a0be2d2877d60461a4ffa00b0b272cd9bddeda05eb0deb8590d343/Telethon-0.17.1.1.tar.gz')
md5sums=('905faf36e3baeb7a0641c78c03ae9adf')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
