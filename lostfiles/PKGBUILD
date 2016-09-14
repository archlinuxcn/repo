# Contributor: graysky <graysky AT archlinux dot us>

pkgname=lostfiles
pkgver=3.25
pkgrel=1
pkgdesc='Find orphaned files not owned by any Arch packages'
arch=('any')
license=('GPL2')
url="https://github.com/graysky2/lostfiles"
source=("https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('1c6a8c8fb98bdda81331ad6df91eb210a7bb8cfc2aa990f55a1b7713917e98c4')

package() {
	cd "$pkgname-$pkgver"
	install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
}
