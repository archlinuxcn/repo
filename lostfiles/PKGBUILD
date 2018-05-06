# Maintainer: graysky <graysky AT archlinux dot us>

pkgname=lostfiles
pkgver=4.02
pkgrel=1
pkgdesc='Find orphaned files not owned by any Arch packages'
arch=('any')
license=('GPL2')
url="https://github.com/graysky2/lostfiles"
source=("$pkgname-$pkgver.tar.xz::https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('f83670cb680935050edcd72f42bf8bc4c9be607ff025ae8960fef997329cedfe')

build() {
  cd "$pkgname-$pkgver"
  make 
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}
