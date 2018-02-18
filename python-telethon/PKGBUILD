_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/cb/45/d4cc33df57576aa601b6f4ca0c79d5689944ef7dc022c4aa92884f02a8fc/Telethon-0.17.3.tar.gz')
md5sums=('fdf54011d6c8a017177653f7a7aee443')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
