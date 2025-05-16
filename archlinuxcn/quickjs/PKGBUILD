# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='Small and embeddable JavaScript engine'
pkgname=quickjs
pkgver=2025.04.26
pkgrel=1
url=https://bellard.org/quickjs
depends=(glibc)
arch=(x86_64)
options=(!strip)
license=(MIT)
_pv="${pkgname}-${pkgver//./-}"
source=("${url}/${_pv}.tar.xz")
sha512sums=('7b9e4316c470f1163abed038ba2919e9367f026f8af8afb07ec07ac98409083c45373126764b526a78651a83e7896d6d05456e60dec46e451315bbeb336da23e')

prepare () {
	cat >> "${_pv}/Makefile" <<-EOF
	CFLAGS += ${CFLAGS}
	LDFLAGS += ${LDFLAGS}
	EOF
}

build () {
	make -C "${_pv}" PREFIX=/usr
}

package () {
	make -C "${_pv}" PREFIX=/usr DESTDIR="${pkgdir}" install

	install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" "${_pv}"/doc/*.*

	# Fixup permissions
	chmod 644 "${pkgdir}"/usr/lib/quickjs/*.a
}
