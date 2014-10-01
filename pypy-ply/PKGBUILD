pkgbase=pypy-ply
pkgname=(pypy3-ply pypy-ply)
pkgver=3.4
pkgrel=1
pkgdesc='Implementation of lex and yacc parsing tools'
arch=('any')
url='http://www.dabeaz.com/ply/'
license=('BSD')
makedepends=('pypy3-setuptools' 'pypy-setuptools')
source=("${url}ply-$pkgver.tar.gz")
sha256sums=('af435f11b7bdd69da5ffbc3fecb8d70a7073ec952e101764c88720cdefb2546b')

prepare() {
  cp -r ply-$pkgver{,-py2}
}

package_pypy3-ply() {
  depends=('pypy3>=2.3' 'pypy3<2.4')

  cd "ply-$pkgver"

  pypy3 setup.py install --root="$pkgdir"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  head -n30 README > "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_pypy-ply() {
  depends=('pypy')

  cd "ply-$pkgver-py2"

  pypy setup.py install --root="$pkgdir"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  head -n30 README > "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
