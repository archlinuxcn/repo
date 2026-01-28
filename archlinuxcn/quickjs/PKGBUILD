# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgdesc='Small and embeddable JavaScript engine'
pkgname=quickjs
pkgver=2025.09.13
pkgrel=1
url=https://bellard.org/quickjs
depends=(glibc)
arch=(x86_64)
options=(!strip)
license=(MIT)
_pv="${pkgname}-${pkgver//./-}"
source=("${url}/${_pv}.tar.xz"
        https://github.com/bellard/quickjs/raw/f1139494d18a2053630c5ed3384a42bb70db3c53/examples/message.json)
sha512sums=('077acba8b318b19cd2660fae0ca03099185b688dba46c89a6456b455639813eefc282975cd1eebdb3c49f62217b9506c6abad86d777b08cb49fe234beef918a2'
            'c3c85602326a50c127b8497876205a4984c9f7a40696e76912943d9c5fd7358d0976a0c8942bfa8b6f45fa7728ca663e072f26b0be94efefe75f224757c7e865')

prepare () {
	cat >> "${_pv}/Makefile" <<-EOF
	CFLAGS += ${CFLAGS}
	LDFLAGS += ${LDFLAGS}
	EOF
	cp message.json "${_pv}/examples/"
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
