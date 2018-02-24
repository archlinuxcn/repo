_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17.4.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/3b/14/136f3c03ea5c8d22aaa9fea1be746c7b07b3bbe1df022ba9cd6cd146c0c9/Telethon-0.17.4.1.tar.gz')
md5sums=('f764f53f32094e31e7c8a291bad1a3a8')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
