# $Id$
# Maintainer: Shang Yuanchun <idealities@gmail.com>

pkgname=mirror
pkgdesc="rsync scheduler for open source mirror site"
pkgver=0.8.0
pkgrel=2
arch=('any')
license=('GPL')
url="https://github.com/ideal/mirror"
depends=('rsync' 'python2-chardet')
source=(https://github.com/ideal/mirror/archive/$pkgver.tar.gz)
md5sums=('fcdb64eed85e17475cc737a9de288cb7')

build() {
    cd $srcdir/$pkgname-$pkgver
    python2 setup.py build
}

package() {
    cd $srcdir/$pkgname-$pkgver
    python2 setup.py install --root=$pkgdir
}
