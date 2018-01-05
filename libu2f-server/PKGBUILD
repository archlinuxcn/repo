# Maintainer: Maxime de Roucy <maxime.deroucy@gmail.com>

pkgname=libu2f-server
pkgver=1.1.0
pkgrel=1
pkgdesc="Yubico Universal 2nd Factor (U2F) Server C Library"
arch=('i686' 'x86_64')
url='https://developers.yubico.com/libu2f-server/'
license=('BSD')
depends=('openssl' 'json-c')
makedepends=('check' 'gengetopt' 'help2man')
source=("https://developers.yubico.com/libu2f-server/Releases/${pkgname}-${pkgver}.tar.xz")

build() {
	cd ${pkgname}-${pkgver}/

	./configure --prefix=/usr
	make
}

check() {
	cd ${pkgname}-${pkgver}/

	make check
}

package() {
	cd ${pkgname}-${pkgver}/

	make DESTDIR="${pkgdir}/" install

	install -D -m0644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}

sha512sums=('ebdb7c8c20727f37f4e31d8f16df7966603374f78478ada723a7b9bec1b0b0622caf6d12a65067ac8651f6088aaad61b2ad6ed51b9d6ef0dc45f031c974d8ff9')
