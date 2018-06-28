_pkgname=Telethon
pkgname=python-telethon
pkgver=1.0.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/4d/d1/f33f34f952c1c64486adb4774e917a4b8b3522660cbb2cad1f3059bb00e3/Telethon-1.0.2.tar.gz')
md5sums=('eb579ee948e9069cdfbee8232dc86c38')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
