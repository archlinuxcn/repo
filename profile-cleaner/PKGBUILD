# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname='profile-cleaner'
pkgver=2.37
pkgrel=1
pkgdesc='Reduces profile size by cleaning their sqlite databases.'
arch=('any')
url='https://github.com/graysky2/profile-cleaner'
license=('MIT')
depends=('bc' 'parallel' 'sqlite')
source=("$pkgname-$pkgver.tar.gz::https://github.com/graysky2/profile-cleaner/archive/v2.37.tar.gz")
install=readme.install
sha256sums=('abdcd2ffab8df9a213654df1e3cbf807799c6e39c147f30a82e1b96e8a36c55d')

build() {
	cd "$pkgname-$pkgver"
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir" install
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
