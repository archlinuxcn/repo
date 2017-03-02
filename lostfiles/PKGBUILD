# Contributor: graysky <graysky AT archlinux dot us>

pkgname=lostfiles
pkgver=3.26
pkgrel=1
pkgdesc='Find orphaned files not owned by any Arch packages'
arch=('any')
license=('GPL2')
url="https://github.com/graysky2/lostfiles"
source=("https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('42c5408b1bbc32eafebf16b0f843c775b39356b6edecdff5437d3e58c1c614ed')

package() {
	cd "$pkgname-$pkgver"
	install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
}
