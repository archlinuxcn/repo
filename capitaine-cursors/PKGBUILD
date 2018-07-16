# Maintainer: Ye Jingchen <ye.jingchen@gmail.com>

pkgname=capitaine-cursors
pkgver=r2.1
pkgrel=1
pkgdesc="An x-cursor theme inspired by macOS and based on KDE Breeze"
arch=('any')
url="https://github.com/keeferrourke/capitaine-cursors"
license=('LGPL3')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/keeferrourke/${pkgname}/archive/${pkgver}.tar.gz")
md5sums=('9633d54feb6ed38af23d8e737131004f')
sha256sums=('70a40f78b6271819815847bb77d3b3b68bed82247b43da8394b3f88d6c05ea00')

package() {
	cd "$pkgname-$pkgver"
	install -dm755 "$pkgdir/usr/share/icons"
	cp -r dist/ "$pkgdir/usr/share/icons/capitaine-cursors"
}
