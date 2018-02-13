_pkgname=asks
pkgname=python-asks
pkgver=1.3.10
pkgrel=1
pkgdesc="asks - async http"
arch=('any')
url="https://github.com/theelous3/asks"
license=('MIT')
depends=('python' 'python-multio' 'python-h11')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/80/22/ef3bafc4d5b7b54cab7da1afd3e2cd73531dc546add635ff72e607058f0d/asks-1.3.10.tar.gz')
md5sums=('1ad73b73ee24ede7f818c9747dcbbb1d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
