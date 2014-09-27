# Maintainer: Jelle van der Waa <jelle@vdwaa.nl>
# Contributer: Allan McRae <allan@archlinux.org>

pkgbase=pypy-six
pkgname=('pypy-six' 'pypy3-six')
pkgver=1.8.0
pkgrel=1
pkgdesc="Python 2 and 3 compatibility utilities"
arch=('any')
url="http://pypi.python.org/pypi/six/"
license=('MIT')
makedepends=('pypy3' 'pypy')
source=(http://pypi.python.org/packages/source/s/six/six-$pkgver.tar.gz)
md5sums=('1626eb24cc889110c38f7e786ec69885')

build() {
  cd "$srcdir"
  cp -r six-$pkgver six2-$pkgver
}

check() {
  cd "$srcdir/six-$pkgver"
  pypy3 setup.py check

  cd "$srcdir/six2-$pkgver"
  pypy setup.py check
}

package_pypy3-six() {
  depends=('pypy3')
  cd "$srcdir/six-$pkgver"
  pypy3 setup.py install --root "${pkgdir}" --optimize=1
  install -Dm644 "${srcdir}/six-${pkgver}/LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_pypy-six() {
  depends=('pypy')
  cd "$srcdir/six2-$pkgver"
  pypy setup.py install --root "${pkgdir}" --optimize=1
  install -Dm644 "${srcdir}/six-${pkgver}/LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
