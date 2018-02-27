_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17.4.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/3b/e2/ade91f05f068c90ab8ce7750df38aa158e9f4a880cc90ca335fff3f389fa/Telethon-0.17.4.3.tar.gz')
md5sums=('66fdad94474bf9a9741ac30886e34bcd')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
