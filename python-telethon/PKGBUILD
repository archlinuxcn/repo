_pkgname=Telethon
pkgname=python-telethon
pkgver=0.18.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/ac/b2/2bc3518696a27f3956909dc5515ce7900abe9806375384aeac5cb706e360/Telethon-0.18.2.tar.gz')
md5sums=('e66ba5a410f57278c71bdd8e92f22174')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
