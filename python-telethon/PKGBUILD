_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.2.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/c6/46/d94750ec2a05386f132dec094df297cd19c4fa8dd78e60ac41aa0638505b/Telethon-0.16.2.2.tar.gz')
md5sums=('3ef2078971169e857677ab03d9803283')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
