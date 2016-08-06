# Maintainer: wicast C <wicastchen at hotmail dot com>

_pypiname=doxytag2zealdb
pkgname=("python2-$_pypiname")
pkgver=0.1.2
pkgrel=1
pkgdesc="create sqlite db for docset from a Doxygen tag file"
arch=(any)
url="http://pypi.python.org/pypi/$_pypiname"
license=('GPLv3')
depends=('python2' 'python2-docopt' 'python2-beautifulsoup4')
makedepends=('python-setuptools' 'python2-setuptools')
source=("doxytag2zealdb.tar.bz2::https://gitlab.com/vedvyas/doxytag2zealdb/repository/archive.tar.bz2?ref=v${pkgver}")
md5sums=('a0945a68c248737005f2358a69de9bfc')



package() {

  cd "$_pypiname-v${pkgver}-d4cef285e34f65de40d4c0bbef0fc5ac39d53c94"
  python2 setup.py install --root="${pkgdir}/" --optimize=1

  install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
