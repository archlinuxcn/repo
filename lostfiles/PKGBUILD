# Maintainer: graysky <graysky AT archlinux dot us>

pkgname=lostfiles
pkgver=4.01
pkgrel=1
pkgdesc='Find orphaned files not owned by any Arch packages'
arch=('any')
license=('GPL2')
url="https://github.com/graysky2/lostfiles"
source=("$pkgname-$pkgver.tar.xz::https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('660eafaac135e12f69fe4cc14850068bed75f5dc24a03bba481712ad12e9d419')

build() {
  cd "$pkgname-$pkgver"
  make 
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}
