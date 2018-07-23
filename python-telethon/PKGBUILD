_pkgname=Telethon
pkgname=python-telethon
pkgver=1.1.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/60/53/1191e4679a5935c6b1342eb895441035bef45eee04c90133b62eae5b1d1f/Telethon-1.1.1.tar.gz')
md5sums=('f6cd2aa3244f83f8f86b36e526eddc5f')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
