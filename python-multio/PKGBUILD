_pkgname=multio
pkgname=python-multio
pkgver=0.1.2
pkgrel=1
pkgdesc="mulio - an unified async library for curio and trio"
arch=('any')
url="https://github.com/theelous3/multio"
license=('MIT')
depends=('python' 'python-multio-provider')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/7d/31/b0e65de4a2ed56594bad8a870251eff62597ea0b4a5eedc0da68069a4bcf/multio-0.1.2.tar.gz')
md5sums=('876e2436c678694ccf03e3777e0368de')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
