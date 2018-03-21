# Maintainer: GreaterFire <GreaterFire at protonmail dot com>
pkgname=trojan
pkgver=1.0.0
pkgrel=1
pkgdesc="An unidentifiable mechanism that helps you bypass GFW."
arch=('x86_64' 'i686' 'armv6h' 'armv7h' 'arm' 'aarch64')
url="https://github.com/trojan-gfw/trojan"
license=('GPL3')
depends=('boost-libs' 'ca-certificates')
makedepends=('cmake' 'boost')
source=("https://github.com/trojan-gfw/$pkgname/archive/v$pkgver.tar.gz")
backup=('etc/trojan.json' 'usr/lib/systemd/system/trojan.service')
sha512sums=('a8b0426f933e7b7f2fd75d8de71f3993f46bd851048bd03a357e35380f89716a294863d60d73219d40a89ab99e9b732181df050e6663b39a7450b7dc598ca92f')
build() {
	cd "$pkgname-$pkgver"
	cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
	make
}
package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
