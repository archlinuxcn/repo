# Maintainer: Maxime de Roucy <maxime.deroucy@gmail.com>

pkgname=libu2f-server
pkgver=1.0.1
pkgrel=1
pkgdesc="Yubico Universal 2nd Factor (U2F) Server C Library"
arch=('i686' 'x86_64')
url='https://developers.yubico.com/libu2f-server/'
license=('BSD')
depends=('openssl' 'json-c')
makedepends=('check')
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

	mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
	cp COPYING "${pkgdir}/usr/share/licenses/${pkgname}/"
}

sha256sums=('a618f59051209d6d70c24cf42d64c9b67bd7dd5946b6dbd2c649181d7e8f1f6e')
