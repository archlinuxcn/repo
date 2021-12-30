# $Id$
# Maintainer: Shang Yuanchun <idealities@gmail.com>

pkgname=mirror
pkgdesc="rsync scheduler for open source mirror site"
pkgver=0.8.2
pkgrel=3
arch=('any')
license=('GPL')
url="https://github.com/ideal/mirror"
depends=('rsync' 'python-chardet')
makedepends=('python-setuptools')
source=(https://github.com/ideal/mirror/archive/$pkgver.tar.gz)
md5sums=('7b45a00295533afc7fb1f2ec3aa9d899')

build() {
    cd $srcdir/$pkgname-$pkgver
    python setup.py build
}

package() {
    cd $srcdir/$pkgname-$pkgver
    python setup.py install --root=$pkgdir
}
