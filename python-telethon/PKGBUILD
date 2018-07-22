_pkgname=Telethon
pkgname=python-telethon
pkgver=1.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/5e/ae/71adef82937ce3382d5a498e8dd4cd6b1bd4a8a00487d6586c4054d2be4e/Telethon-1.1.tar.gz')
md5sums=('48978be93fe93a78bed6c95773aadf8c')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
