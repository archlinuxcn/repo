_pkgname=Telethon
pkgname=python-telethon
pkgver=0.15.5.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/7c/2f/5ee8b7b0e87e7cc5b4c2834e605bfb83061f6f9c2b1e1f2d56eb1dd76246/Telethon-0.15.5.1.tar.gz')
md5sums=('253b930edef712ae752327959d3cdce6')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
