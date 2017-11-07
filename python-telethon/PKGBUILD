_pkgname=Telethon
pkgname=python-telethon
pkgver=0.15.4.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/02/47/6c1710bb019f2a9241be78403646b8a9f17ad390fe4defa318b8029c1356/Telethon-0.15.4.1.tar.gz')
md5sums=('451348f1196f36a0e39bae43149b65e6')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
