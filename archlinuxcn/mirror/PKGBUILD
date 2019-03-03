# $Id$
# Maintainer: Shang Yuanchun <idealities@gmail.com>

pkgname=mirror
pkgdesc="rsync scheduler for open source mirror site"
pkgver=0.7.8
pkgrel=1
arch=('any')
license=('GPL')
url="https://github.com/ideal/mirror"
depends=('rsync' 'python2-chardet')
source=(https://github.com/ideal/mirror/archive/$pkgver.tar.gz)
md5sums=('350bbd56db4399a5665ccbd0f67baf61')

build() {
    cd $srcdir/$pkgname-$pkgver
    python2 setup.py build
}

package() {
    cd $srcdir/$pkgname-$pkgver
    python2 setup.py install --root=$pkgdir
}
