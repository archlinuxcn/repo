_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/48/39/6e998c4b0e0eceb6cbf1809326dfd8ce81a89257a727001f6145ea20e047/Telethon-0.17.1.tar.gz')
md5sums=('3ec7f155cc63e92985fd0ceaa8d75565')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
