_pkgname=Telethon
pkgname=python-telethon
pkgver=0.18.0.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/5c/17/062cffdc808ed8ef6cd471fca71b01d76a14db3ba5b8adbf39b633493632/Telethon-0.18.0.3.tar.gz')
md5sums=('191e1f30919a2d3fea10349119248614')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
