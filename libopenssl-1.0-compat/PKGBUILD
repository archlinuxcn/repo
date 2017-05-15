# Maintainer: Michael Straube <straubem@gmx.de>
# Contributor: Pierre Schmitz <pierre@archlinux.de>

pkgname=libopenssl-1.0-compat
_ver=1.0.2k
# use a pacman compatible version scheme
pkgver=${_ver/[a-z]/.${_ver//[0-9.]/}}
pkgrel=3
pkgdesc='The Open Source library for Secure Sockets Layer and Transport Layer Security (without versioned symbols patch)'
arch=('i686' 'x86_64')
url='https://www.openssl.org'
license=('custom:BSD')
depends=('perl')
optdepends=('ca-certificates')
options=('!makeflags')
source=("https://www.openssl.org/source/openssl-${_ver}.tar.gz"
        "https://www.openssl.org/source/openssl-${_ver}.tar.gz.asc"
        "no-rpath.patch"
        "ssl3-test-failure.patch")
sha256sums=('6b3977c61f2aedf0f96367dcfb5c6e578cf37e7b8d913b4ecb6643c3cb88d8c0'
            'SKIP'
            '754d6107a306311e15a1db6a1cc031b81691c8b9865e8809ac60ca6f184c957c'
            'c54ae87c602eaa1530a336ab7c6e22e12898e1941012349c153e52553df64a13')
validpgpkeys=('8657ABB260F056B1E5190839D9C4D26D0E604491') # Matt Caswell

prepare() {
	cd openssl-$_ver

	# remove rpath: http://bugs.archlinux.org/task/14367
	patch -p0 -i ../no-rpath.patch

	# disable a test that fails when ssl3 is disabled
	patch -p1 -i ../ssl3-test-failure.patch
}

build() {
	cd openssl-$_ver

	if [ "${CARCH}" == 'x86_64' ]; then
		openssltarget='linux-x86_64'
		optflags='enable-ec_nistp_64_gcc_128'
	elif [ "${CARCH}" == 'i686' ]; then
		openssltarget='linux-elf'
		optflags=''
	fi

	# mark stack as non-executable: http://bugs.archlinux.org/task/12434
	./Configure --prefix=/usr --openssldir=/etc/ssl --libdir=lib/openssl-1.0 \
		shared no-ssl3-method ${optflags} \
		"${openssltarget}" \
		"-Wa,--noexecstack ${CPPFLAGS} ${CFLAGS} ${LDFLAGS}"

	make depend
	make
}

check() {
	cd openssl-$_ver
	make test
}

package() {
	cd openssl-$_ver
	install -Dm755 libcrypto.so.1.0.0 "$pkgdir/usr/lib/libcrypto-compat.so.1.0.0"
	install -Dm755 libssl.so.1.0.0 "$pkgdir/usr/lib/libssl-compat.so.1.0.0"
	install -d "$pkgdir/usr/lib/openssl-1.0-compat"
	for _i in so so.1.0.0; do
		ln -sf ../libssl-compat.so.1.0.0 "$pkgdir/usr/lib/openssl-1.0-compat/libssl.${_i}"
		ln -sf ../libcrypto-compat.so.1.0.0 "$pkgdir/usr/lib/openssl-1.0-compat/libcrypto.${_i}"
	done
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
