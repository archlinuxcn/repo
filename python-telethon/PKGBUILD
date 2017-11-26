_pkgname=Telethon
pkgname=python-telethon
pkgver=0.15.5.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/ba/ab/fe667074e379a4482683f2c83b39587ff8d16c500da57284e53b6df1d224/Telethon-0.15.5.3.tar.gz')
md5sums=('e27fdc7224394ea817f6c84f7b2edc1e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
