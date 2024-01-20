# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='Small and embeddable JavaScript engine'
pkgname=quickjs
pkgver=2024.01.13
pkgrel=1
url=https://bellard.org/quickjs
depends=(glibc)
arch=(x86_64)
options=(!strip)
license=(MIT)
_pv="${pkgname}-${pkgver//./-}"
source=("${url}/${_pv}.tar.xz")
sha512sums=('9f426404e4dc1e2a41fcc235b72e58708041aed24eadd5fb9e82f62435501003d3a6b04831f307b04852551d2fd265b94cd400b3293ec0810465f52de8a6c057')

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
