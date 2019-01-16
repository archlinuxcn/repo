_pkgname=uniout
pkgname=python2-uniout
pkgver=0.3.7
pkgrel=1
pkgdesc="Never see escaped bytes in output."
arch=('any')
url="https://github.com/moskytw/uniout"
license=('MIT')
depends=('python2')
makedepends=('python2-setuptools')
source=('https://pypi.python.org/packages/source/u/uniout/uniout-0.3.7.tar.gz')
md5sums=('3df45169da988df040f21608c9c4346b')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python2 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python2 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
