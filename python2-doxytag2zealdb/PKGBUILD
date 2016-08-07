# Maintainer: wicast C <wicastchen at hotmail dot com>

_pypiname=doxytag2zealdb
pkgname=("python2-$_pypiname")
pkgver=0.1.2
pkgrel=2
pkgdesc="create sqlite db for docset from a Doxygen tag file"
arch=(any)
url="http://pypi.python.org/pypi/$_pypiname"
license=('GPLv3')
depends=('python2' 'python2-docopt' 'python2-beautifulsoup4')
makedepends=('python-setuptools' 'python2-setuptools')
source=("git+https://gitlab.com/vedvyas/doxytag2zealdb.git#tag=v${pkgver}")
md5sums=(SKIP)


package() {

  cd "$_pypiname"
  python2 setup.py install --root="${pkgdir}/" --optimize=1

  install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
