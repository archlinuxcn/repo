# $Id$
# Maintainer: Fabien Devaux <fdev31 at gmail dot com>

_py=python2
_n=pyScss

pkgname=$_py-pyscss
pkgver=1.3.4
pkgrel=4
pkgdesc="a Scss compiler for Python"
depends=($_py  "$_py-six" "python2-pathlib" "python2-enum34")
makedepends=($_py "$_py-distribute")
arch=('any')
source=(http://pypi.python.org/packages/source/${_n:0:1}/$_n/$_n-$pkgver.tar.gz)
md5sums=('9527b4864cd6023f77a8277e6fb773d7')
url="http://pypi.python.org/pypi/pyScss"
license=("MIT")


package() {
    cd $srcdir/$_n-$pkgver
    $_py setup.py build  || return 1
    $_py setup.py install --root="$pkgdir/" --optimize=1
}

