_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.1.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/31/78/073a7f978b170ace3d0d53d80e237655c5f7c7eeeefb19c579a4b99cbf03/Telethon-0.16.1.3.tar.gz')
md5sums=('730a2947e684563e6fc4769fc70b202b')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
