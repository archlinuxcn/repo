_pkgname=butterfly
pkgname=butterfly
pkgver=3.2.4
pkgrel=1
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="https://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=('https://files.pythonhosted.org/packages/0d/5a/e3bdadf785794e50eb08ec793473bd3884ced62de9a356ab057ab965f3cb/butterfly-3.2.4.tar.gz')
md5sums=('6585419e02c0204c6aabdc0d2f445d5d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
