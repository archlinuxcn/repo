_pkgname=butterfly
pkgname=butterfly
pkgver=3.0.2
pkgrel=1
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="https://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=('https://pypi.python.org/packages/0b/f6/2331df1a5def7597028ce4dd095afc8cc0b7aaa537673cafdbbd55c8ffd4/butterfly-3.0.2.tar.gz')
md5sums=('b1fe954e68abc5ea39bc69deaa491966')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
