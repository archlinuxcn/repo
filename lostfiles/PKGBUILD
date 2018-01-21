# Contributor: graysky <graysky AT archlinux dot us>

pkgname=lostfiles
pkgver=3.27
pkgrel=1
pkgdesc='Find orphaned files not owned by any Arch packages'
arch=('any')
license=('GPL2')
url="https://github.com/graysky2/lostfiles"
source=("$pkgname-$pkgver.tar.xz::https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('0095834e4398abbb1cbdd93a500dc1262665d3d9467817abaaf4f8e82ed17cfa')

package() {
	cd "$pkgname-$pkgver"
	install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
}
