# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname='profile-cleaner'
pkgver=2.36
pkgrel=1
pkgdesc='Reduces profile size by cleaning their sqlite databases.'
arch=('any')
url='https://github.com/graysky2/profile-cleaner'
license=('MIT')
depends=('bc' 'parallel' 'sqlite')
source=("http://repo-ck.com/source/$pkgname/$pkgname-$pkgver.tar.xz")
install=readme.install
sha256sums=('a8b10fd212e0b0011e020bb3e65889970dcf0db043776358ca31bb3675b76279')

build() {
	cd "$pkgname-$pkgver"
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir" install
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
