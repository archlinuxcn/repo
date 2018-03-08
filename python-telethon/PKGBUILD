_pkgname=Telethon
pkgname=python-telethon
pkgver=0.18.0.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/07/a3/6d4c3efdbb3b085c7ef46fe720df50cf201ed76bec42d62a7f869b38fe8c/Telethon-0.18.0.1.tar.gz')
md5sums=('711a86fbedf21c53c27a61e00976dcbc')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
