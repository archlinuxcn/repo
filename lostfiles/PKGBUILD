# Contributor: graysky <graysky AT archlinux dot us>

pkgname=lostfiles
pkgver=4.00
pkgrel=1
pkgdesc='Find orphaned files not owned by any Arch packages'
arch=('any')
license=('GPL2')
url="https://github.com/graysky2/lostfiles"
source=("$pkgname-$pkgver.tar.xz::https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('4245e8dcc342e96ad10a24f30e74ecbfa56dbc69bf3f0dd36cd70266b90883fa')

package() {
	cd "$pkgname-$pkgver"
	install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
}
