# $Id$
# Maintainer: Fabien Devaux <fdev31 at gmail dot com>

_py=python2
_n=pyScss

pkgname=$_py-pyscss
pkgver=1.3.5
pkgrel=1
pkgdesc="a Scss compiler for Python"
depends=($_py  "$_py-six" "python2-pathlib" "python2-enum34")
makedepends=($_py "$_py-distribute")
arch=('any')
source=("https://pypi.python.org/packages/01/7b/c6bfb2515ed08cbfb76b0e72254f24caf76f25676d72024837a85a1e68f5/pyScss-1.3.5.tar.gz#md5=b349a750ac77033d8e6b6de1d6912263")
md5sums=('b349a750ac77033d8e6b6de1d6912263')
url="http://pypi.python.org/pypi/pyScss"
license=("MIT")


package() {
    cd $srcdir/$_n-$pkgver
    $_py setup.py build  || return 1
    $_py setup.py install --root="$pkgdir/" --optimize=1
}

