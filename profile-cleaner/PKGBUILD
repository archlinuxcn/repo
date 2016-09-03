# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname='profile-cleaner'
pkgver=2.35
pkgrel=1
pkgdesc='Reduces profile size by cleaning their sqlite databases.'
arch=('any')
url='https://github.com/graysky2/profile-cleaner'
license=('MIT')
depends=('bc' 'parallel' 'sqlite')
source=("http://repo-ck.com/source/$pkgname/$pkgname-$pkgver.tar.xz")
install=readme.install
sha256sums=('d02f31fb0c5a7a07da33c8e9f1ccc3d814f2ddefa427d4b3422889b54fcdb92f')

build() {
	cd "$pkgname-$pkgver"
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir" install
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
