pkgbase=pypy-pyserial
pkgname=('pypy3-pyserial' 'pypy-pyserial')
pkgver=2.7
pkgrel=4
pkgdesc="Multiplatform Serial Port Module for Python"
arch=('any')
url="http://pyserial.sf.net"
license=('custom:PYTHON')
makedepends=('pypy3' 'pypy')
source=(http://pypi.python.org/packages/source/p/pyserial/pyserial-$pkgver.tar.gz)
md5sums=('794506184df83ef2290de0d18803dd11')

build() {
  cp -a $srcdir/pyserial-$pkgver $srcdir/py2serial-$pkgver
}

package_pypy3-pyserial() {
  depends=('pypy3>=2.3' 'pypy3<2.4')

  cd "$srcdir"/pyserial-$pkgver
  pypy3 setup.py install --root="$pkgdir"
  install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.txt

  install -dm755 "${pkgdir}/usr"
  mv "${pkgdir}/opt/pypy3/bin" "${pkgdir}/usr"
  mv "$pkgdir"/usr/bin/miniterm.py "$pkgdir"/usr/bin/miniterm-pypy3.py
}

package_pypy-pyserial() {
  depends=('pypy')

  cd "$srcdir"/py2serial-$pkgver
  pypy setup.py install --root="$pkgdir"
  install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.txt

  install -dm755 "${pkgdir}/usr"
  mv "${pkgdir}/opt/pypy/bin" "${pkgdir}/usr"
  mv "$pkgdir"/usr/bin/miniterm.py "$pkgdir"/usr/bin/miniterm-pypy.py
}
