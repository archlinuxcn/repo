# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgbase=python-planout
pkgname=(python2-planout)  # python-planout
_pkgname=planout
pkgver=0.5
pkgrel=1
pkgdesc="A framework for online field experimentation"
arch=('any')
url='http://facebook.github.io/planout'
license=('custom:BSD')
makedepends=('python' 'python2')
checkdepends=('python-pytest' 'python2-pytest')
source=("https://pypi.python.org/packages/source/P/PlanOut/PlanOut-$pkgver.tar.gz"
        LICENSE)
sha512sums=('2dee30faa2602fb74cc8de76eacfaa7d7cc7bec64cd4960c6076eded420cffd7e6828bc01e0a60b885e0be14c719124e524f3d7ab5b21cb14854e7e47b9edf55'
            '6198f89c3f63d659c8ebb32f925c9ac83043bd73c5b569b2ec782da608e532ef7c57c4e481f728b3aa75869e940e9e96add2096fd8565b637c12fe7506ee01c9')

prepare() {
  cp -a PlanOut-$pkgver{,-py2}
}

build() {
  # cd "$srcdir/PlanOut-$pkgver"
  # python setup.py build

  cd "$srcdir/PlanOut-$pkgver-py2"
  python2 setup.py build
}

check() {
  cd "$srcdir/PlanOut-$pkgver/planout/test"
  # py.test

  cd "$srcdir/PlanOut-$pkgver-py2/planout/test"
  py.test2
}

package_python-planout() {
  depends=('python')

  cd PlanOut-$pkgver
  python setup.py install -O1 --root "$pkgdir"

  install -Dm644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_python2-planout() {
  depends=('python2')

  cd PlanOut-$pkgver-py2
  python2 setup.py install -O1 --root "$pkgdir"

  install -Dm644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
