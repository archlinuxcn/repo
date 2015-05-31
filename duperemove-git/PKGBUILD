# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>

pkgname=duperemove-git
pkgver=300.da5f1db
pkgrel=1
pkgdesc="Btrfs extent deduplication utility"
arch=('any')
url="https://github.com/markfasheh/duperemove"
license=('GPL')
depends=('glib2' 'sqlite')
makedepends=('git')
conflicts=('duperemove')
source=("$pkgname"::'git://github.com/markfasheh/duperemove.git#branch=master')
md5sums=( 'SKIP' )

pkgver() {
  cd ${pkgname}
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
  cd "$srcdir/$pkgname"
  make
}

package() {
  cd $srcdir/$pkgname
  install -Dm755 ./duperemove $pkgdir/usr/bin/duperemove
  install -Dm644 ./duperemove.8 $pkgdir/usr/share/man/man8/duperemove.8
}
