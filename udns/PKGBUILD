# Maintainer: Christian Hesse <mail@eworm.de>
# Contributor: Gaetan Bisson <bisson@archlinux.org>

pkgname=udns
pkgver=0.4
pkgrel=1
pkgdesc='Stub DNS resolver library with ability to perform both syncronous and asyncronous DNS queries'
url='http://www.corpit.ru/mjt/udns.html'
license=('LGPL')
arch=('i686' 'x86_64' 'armv6h')
source=("http://www.corpit.ru/mjt/udns/udns-${pkgver}.tar.gz")

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	./configure
	make
	make sharedlib
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	install -D -m0755 dnsget "${pkgdir}/usr/bin/dnsget"
	install -D -m0755 rblcheck "${pkgdir}/usr/bin/rblcheck"
	install -D -m0755 ex-rdns "${pkgdir}/usr/bin/ex-rdns"

	install -D -m0644 udns.h "${pkgdir}/usr/include/udns.h"
	install -D -m0755 libudns.so.0 "${pkgdir}/usr/lib/libudns.so.0"
	ln -s libudns.so.0 "${pkgdir}/usr/lib/libudns.so"

	install -D -m0644 dnsget.1 "${pkgdir}/usr/share/man/man1/dnsget.1"
	install -D -m0644 rblcheck.1 "${pkgdir}/usr/share/man/man1/rblcheck.1"
	install -D -m0644 udns.3 "${pkgdir}/usr/share/man/man3/udns.3"
}

sha256sums=('115108dc791a2f9e99e150012bcb459d9095da2dd7d80699b584ac0ac3768710')
