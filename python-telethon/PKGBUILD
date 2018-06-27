_pkgname=Telethon
pkgname=python-telethon
pkgver=1.0.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/82/07/e55d2895fc0599e78f3cd7b79dcf0426693385ed92d1625f52fccc621e92/Telethon-1.0.1.tar.gz')
md5sums=('b8e6b1910d927447e367913b73debcc8')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
