# Maintainer: Christian Hesse <mail@eworm.de>
# Contributor: trya <tryagainprod@gmail.com>
# Contributor: Pierre Schmitz <pierre@archlinux.de>

_pkgbasename=openssl
pkgname=openssl098
_ver=0.9.8zg
# use a pacman compatible version scheme
pkgver=${_ver/[a-z]*/.${_ver//[0-9.]/}}
pkgrel=2
pkgdesc='The Open Source toolkit for Secure Sockets Layer and Transport Layer Security (0.9.8 branch)'
arch=('i686' 'x86_64')
url='https://www.openssl.org'
license=('custom:BSD')
depends=($_pkgbasename)
makedepends=('perl')
optdepends=('ca-certificates')
provides=('openssl-compatibility')
conflicts=('openssl-compatibility')
options=(!makeflags)
validpgpkeys=('8657ABB260F056B1E5190839D9C4D26D0E604491')
source=("https://www.openssl.org/source/${_pkgbasename}-${_ver}.tar.gz"{,.asc}
        'no-rpath.patch'
        'ca-dir.patch')

build() {
	cd "${srcdir}/${_pkgbasename}-${_ver}"

	# remove rpath: http://bugs.archlinux.org/task/14367
	patch -p0 -i "${srcdir}/no-rpath.patch"
	# set ca dir to /etc/ssl by default
	patch -p0 -i "${srcdir}/ca-dir.patch"

	# mark stack as non-executable: http://bugs.archlinux.org/task/12434
	./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib \
		shared zlib enable-md2 -Wa,--noexecstack

	# fix cross compilation (and possibly more...)
	sed -i '/^CFLAG=/s/$/ $(CFLAGS)/' Makefile

	make
}

package() {
	cd "${srcdir}/${_pkgbasename}-${_ver}"

	install -D -m0755 libssl.so.0.9.8 "${pkgdir}/usr/lib/libssl.so.0.9.8"
	install -D -m0755 libcrypto.so.0.9.8 "${pkgdir}/usr/lib/libcrypto.so.0.9.8"
	install -D -m0755 apps/openssl "${pkgdir}/usr/bin/openssl098"

	mkdir -p "${pkgdir}/usr/share/licenses"
	ln -s ${_pkgbasename} "${pkgdir}/usr/share/licenses/${pkgname}"
}

sha256sums=('06500060639930e471050474f537fcd28ec934af92ee282d78b52460fbe8f580'
            'SKIP'
            '754d6107a306311e15a1db6a1cc031b81691c8b9865e8809ac60ca6f184c957c'
            '9e8126f3a748f4c1d6fe34d4436de72b16a40e97a6d18234d2e88caa179d50c4')
