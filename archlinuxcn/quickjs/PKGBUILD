# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='Small and embeddable JavaScript engine'
pkgname=quickjs
pkgver=2021.03.27
pkgrel=1
url=https://bellard.org/quickjs
depends=(gcc-libs)
arch=(x86_64)
options=(!strip)
license=(custom:MIT)
_pv="${pkgname}-${pkgver//./-}"
source=("${url}/${_pv}.tar.xz")
sha512sums=('eeb810083484df213bc658a8703ca3ef094b7789c2b49eed86cb4068c9f9da401ad0300261d61a163c6ea82306f3ef50bf8e29a64920f704fd8958ef08a7286c')

prepare () {
	cat >> "${_pv}/Makefile" <<-EOF
	CFLAGS += ${CFLAGS}
	LDFLAGS += ${LDFLAGS}
	EOF
}

build () {
	make -C "${_pv}" prefix=/usr
}

package () {
	make -C "${_pv}" prefix="${pkgdir}/usr" install

	install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" "${_pv}"/doc/*.*

	# Fixup permissions
	chmod 644 "${pkgdir}"/usr/lib/quickjs/*.a
}
