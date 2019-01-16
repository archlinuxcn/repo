# Maintainer: Maxime de Roucy <maxime.deroucy@gmail.com>
# Contributor: David Manouchehri <manouchehri@riseup.net>
# Contributor: Sven Lechner <SirWindfield@users.noreply.github.com>

pkgname=pam_u2f
pkgver=1.0.7
pkgrel=1
pkgdesc="Universal 2nd Factor (U2F) PAM authentication module from Yubico"
arch=('i686' 'x86_64')
url='https://developers.yubico.com/pam-u2f/'
license=('BSD')
depends=('libu2f-host' 'libu2f-server')
makedepends=('asciidoc')
source=("https://developers.yubico.com/${pkgname/_/-}/Releases/${pkgname}-${pkgver}.tar.gz")
sha512sums=('5b8fe116782684e5da395a4923b4c300b0d4b6d9e297c8de5cc4ca2ed633fda30cdbc4ae6bbb8a582faf8068dbed13048a2b2f742ebe9eea208fbb7a407caf0a')

build() {
	cd ${pkgname}-${pkgver}/

	./configure \
		--prefix=/usr \
		--with-pam-dir=/usr/lib/security
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

# vim:set et sw=2 sts=2 tw=80:
