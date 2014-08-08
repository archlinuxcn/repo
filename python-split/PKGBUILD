# Maintainer: Felix Yan <felixonmars@gmail.com>

pkgbase=python-split
pkgname=("python-split" "python2-split")
pkgver=0.3
pkgrel=1
pkgdesc="Functions to split or partition sequences"
arch=('any')
url="https://bitbucket.org/astanin/python-split"
license=('MIT')
makedepends=('python' 'python2')
source=("https://pypi.python.org/packages/source/s/split/split-$pkgver.tar.gz")
md5sums=('b7335dd97e4dda7ba6d3098ee6202612')

prepare() {
  cp -a "split-$pkgver"{,-py2}
}

package_python-split() {
  depends=('python')

  cd split-$pkgver
  python setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_python2-split() {
  depends=('python2')

  cd split-$pkgver-py2
  python2 setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
