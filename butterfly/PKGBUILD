_pkgname=butterfly
pkgname=butterfly
pkgver=3.0.3
pkgrel=1
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="https://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=('https://pypi.python.org/packages/f3/5f/cefa2dc9a5fe8fce4e5bd56231b4ad8635b2708c6c15985c50e48ff07193/butterfly-3.0.3.tar.gz')
md5sums=('052db88dbb2fc6c9ce8c4bd7f27d7011')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
