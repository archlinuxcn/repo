# Maintainer: Rafael Fontenelle <rafaeff@gnome.org>

_name=jsmin
pkgname=('python-jsmin' 'python2-jsmin')
pkgbase=python-$_name
pkgver=2.2.2
pkgrel=3
pkgdesc="JavaScript minifier"
arch=(any)
url="https://pypi.org/pypi/$_name"
license=('MIT')
makedepends=('python-setuptools' 'python2-setuptools')
source=("https://pypi.org/packages/source/${_name:0:1}/$_name/$_name-$pkgver.tar.gz")
md5sums=('00e7a3179a4591aab2ee707b3214e2fd')

prepare() {
  cp -a $_name-$pkgver{,-py2}
}

build() {
  cd "$srcdir/$_name-$pkgver"
  python setup.py build

  cd "$srcdir/$_name-$pkgver-py2"
  python2 setup.py build
}

package_python-jsmin() {
  depends=('python')
  cd "$srcdir/$_name-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
  install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}

package_python2-jsmin() {
  depends=('python2')
  cd "$srcdir/$_name-$pkgver-py2"
  python2 setup.py install --root="$pkgdir/" --optimize=1 --skip-build
  install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}
