_pkgname=Telethon
pkgname=python-telethon
pkgver=0.18.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/d2/56/0f08996b6405d9855f7340638ffe49c0b91fb899cd020c0aa3c00354ba92/Telethon-0.18.1.tar.gz')
md5sums=('3fbaf5842ddabfc6bec9a3fdac7c051b')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
