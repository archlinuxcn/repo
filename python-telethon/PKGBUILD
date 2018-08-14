_pkgname=Telethon
pkgname=python-telethon
pkgver=1.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/f4/b2/98c2b4f9eb8026109a6ffeb1e5e7c2b8e40260dee639ab02e5b0df1bd337/Telethon-1.2.tar.gz')
md5sums=('19ea4e80371e10bee0583a2c491c9491')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
