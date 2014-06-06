# $Id: PKGBUILD 112722 2014-06-05 15:38:12Z pierre $
# Upstream Maintainer: Pierre Schmitz <pierre@archlinux.de>
# Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=openssl
pkgname=libx32-$_pkgbasename
_ver=1.0.1h
# use a pacman compatible version scheme
pkgver=${_ver/[a-z]/.${_ver//[0-9.]/}}
#pkgver=$_ver
pkgrel=1
pkgdesc='The Open Source toolkit for Secure Sockets Layer and Transport Layer Security (x32 ABI)'
arch=('x86_64')
url='https://www.openssl.org'
license=('custom:BSD')
depends=('libx32-zlib' "${_pkgbasename}")
optdepends=('ca-certificates')
makedepends=('gcc-multilib-x32')
options=('!makeflags')
source=("https://www.openssl.org/source/${_pkgbasename}-${_ver}.tar.gz"
        "https://www.openssl.org/source/${_pkgbasename}-${_ver}.tar.gz.asc"
        'no-rpath.patch'
        'ca-dir.patch'
        'openssl-1.0.1-x32.patch'
        'opensslconf-stub.h'
)
md5sums=('8d6d684a9430d5cc98a62a5d8fbda8cf'
         'SKIP'
         'dc78d3d06baffc16217519242ce92478'
         '3bf51be3a1bbd262be46dc619f92aa90'
         '10d0cebf2d9c0f64c307e82542f519e3'
         'dbb0b2e285f9ba95f189a0eaf3586011')

prepare() {
	cd $srcdir/$_pkgbasename-$_ver

    # x32 patch
    patch -p1 -i $srcdir/openssl-1.0.1-x32.patch

	# remove rpath: http://bugs.archlinux.org/task/14367
	patch -p0 -i $srcdir/no-rpath.patch
	# set ca dir to /etc/ssl by default
	patch -p0 -i $srcdir/ca-dir.patch
}

build() {
	export CC="gcc -mx32"
	export CXX="g++ -mx32"
	export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

	cd $srcdir/$_pkgbasename-$_ver

	# mark stack as non-executable: http://bugs.archlinux.org/task/12434
	./Configure --prefix=/usr --openssldir=/etc/ssl --libdir=libx32 \
		shared zlib \
		linux-x32 \
		"-Wa,--noexecstack ${CPPFLAGS} ${CFLAGS} ${LDFLAGS}"

	make MAKEDEPPROG="${CC}" depend
	make
}

check() {
	cd $srcdir/$_pkgbasename-$_ver
	# the test fails due to missing write permissions in /etc/ssl
	# revert this patch for make test
	patch -p0 -R -i $srcdir/ca-dir.patch
	make test
	patch -p0 -i $srcdir/ca-dir.patch
}

package() {
    install="${pkgname}.install"

	cd $srcdir/$_pkgbasename-$_ver
	make INSTALL_PREFIX=$pkgdir install_sw

    mv "${pkgdir}/usr/include/openssl/opensslconf.h" "${srcdir}/opensslconf-x32.h"
	rm -rf ${pkgdir}/{usr/{include,bin},etc}
    install -Dm644 "${srcdir}/opensslconf-x32.h" "${pkgdir}/usr/include/openssl/opensslconf-x32.h"
    install -Dm644 "${srcdir}/opensslconf-stub.h" "${pkgdir}/usr/include/openssl/opensslconf-stub.h"

	mkdir -p $pkgdir/usr/share/licenses
	ln -s $_pkgbasename $pkgdir/usr/share/licenses/$pkgname
}
