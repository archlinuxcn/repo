# $Id: PKGBUILD 208854 2014-03-27 14:43:36Z fyan $
# Maintainer: Felix Yan <felixonmars@gmail.com>
# Contributor: Justin Dray <justin@dray.be>
# Contributor: Alexander Rødseth <rodseth@gmail.com>
# Contributor: lang2 <wenzhi.liang@gmail.com>

pkgbase=pypy-pycparser
pkgname=(pypy3-pycparser pypy-pycparser)
pkgver=2.10
pkgrel=1
pkgdesc='C parser and AST generator written in Python'
url='https://github.com/eliben/pycparser'
makedepends=('pypy3-ply' 'pypy-ply')
arch=('any')
license=('BSD')
source=('https://github.com/eliben/pycparser/archive/release_v2.10.zip')
sha256sums=('1217244f882c330782f4762a1fb37cef21a929ce0123ac388e7e367c35ddbae3')

prepare() {
  cp -r pycparser-release_v${pkgver}{,-py2}
}

build() {
  cd pycparser-release_v${pkgver}
  pypy3 setup.py build

  cd pycparser
  pypy3 _build_tables.py

  cd "$srcdir/pycparser-release_v${pkgver}-py2"
  pypy setup.py build

  cd pycparser
  pypy _build_tables.py
}

package_pypy3-pycparser() {
  depends=('pypy3>=2.3' 'pypy3<2.4' 'pypy3-ply')

  cd pycparser-release_v${pkgver}

  pypy3 setup.py install --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_pypy-pycparser() {
  depends=('pypy-ply')

  cd pycparser-release_v${pkgver}-py2

  pypy setup.py install --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
