# Maintainer: Ľubomír 'the-k' Kučera <lubomir.kucera.jr at gmail.com>
# Contributor: Pierre Schmitz <pierre@archlinux.de>

pkgname=openssl-1.1
_pkgname=openssl
_ver=1.1.1w
# use a pacman compatible version scheme
pkgver=${_ver/[a-z]/.${_ver//[0-9.]/}}
pkgrel=9
pkgdesc='The Open Source toolkit for Secure Sockets Layer and Transport Layer Security'
arch=('aarch64' 'x86_64')
url='https://www.openssl.org'
license=('custom:BSD')
depends=('glibc')
provides=('libcrypto.so' 'libssl.so')
makedepends=('perl')
source=(
	"https://www.openssl.org/source/${_pkgname}-${_ver}.tar.gz"{,.asc}
	'ca-dir.patch'
	# https://salsa.debian.org/debian/openssl/-/tree/debian/bullseye/debian/patches
	CVE-2023-5678.patch
	CVE-2024-0727-1.patch
	CVE-2024-0727-2.patch
	CVE-2024-2511.patch
	CVE-2024-4741.patch
	CVE-2024-5535-1.patch
	CVE-2024-5535-2.patch
	CVE-2024-5535-3.patch
	CVE-2024-5535-4.patch
	CVE-2024-5535-5.patch
	CVE-2024-5535-6.patch
	CVE-2024-5535-7.patch
	CVE-2024-5535-8.patch
	CVE-2024-9143.patch
	CVE-2024-13176.patch
	CVE-2025-9230.patch
	CVE-2025-68160.patch
	CVE-2025-69418.patch
	CVE-2025-69420.patch
	CVE-2025-69421.patch
	CVE-2026-22795_CVE-2026-22796.patch
	# https://git.almalinux.org/rpms/openssl/src/branch/c8s
	CVE-2025-69419-1.patch
	CVE-2025-69419-2.patch
)
sha256sums=('cf3098950cb4d853ad95c0841f1f9c6d3dc102dccfcacd521d93925208b76ac8'
            'SKIP'
            '75aa8c2c638c8a3ebfd9fa146fc61c7ff878fc997dc6aa10d39e4b2415d669b2'
            '2fc41792a80991df8de4174a59888d2217c2d2f57ea0b411ff2c193871389709'
            '26fb539e30ffcdda179bca5c44858df360035e5209facb5cc6e3976129e10de5'
            '84be27ad8732556d880b3b584371dd1603fdbfbe5615990e256ac1b5e00e5163'
            '4bb00c132ad7057bedd91d34a3354087e8a4e3f321acb4b9721e13f89bccd990'
            '6bb37fc0a0b031876c79f6fecf21fd1b3a4fafdc73b0a83bb1ebf407b8b6ac8d'
            'bd0818c56353d04eb61e4f1996e63020597ea44f1c1e014eadccf528fae74304'
            '76f426f62acaec2631172838f7807a91d0d4d05eb05dffe624de3f9c849dbb72'
            '9b1346d6b446ea9c8a9fc67596442bb148ee9aa548d2788fd056ad9d7cbd81e3'
            '8599fe7b8257f42642d0ee879577e4087cd7fa80e6dd2308a105cb767f17dddf'
            'c597f50b8ec0332ecbe5945ba3ca8cde9654d2be3860ecb949293ed75bba23dc'
            '9eaa7c529bf29183a3313a81c80f5b31ec5dd7ed03d154a8cda1f5cae95eba5a'
            'dac937ebd37ed3a9b7bd7d4e646da227eacd2dd46975ffe887bc78ee2d836699'
            'c8ea09e1e68ca794be78a8000d9986759df793c5f929db76b1177e06ca04c61e'
            '1dc2e3b31a3c70cd9f10ec4a1c87f8cfb6776f9cec9cfb99560598679e9b3e88'
            '828792284bd823a0ea6d23033990bd155c8627cdb7200aaf4e6b4bf1d41f4f9d'
            '2bfc4da1ca00791bf268de8d8681b86fcbc4fc9e3949e59dfee36b28b64c920d'
            '2e548f306c136caefcbcc9a3945134bec0171ec88210b708f68490c9ecd9329f'
            '1bb720f06bfc27216e2ac339cd13d94a1269db3e97c80e734e649ed4e8245473'
            'a8872bd2e35b9e98f609280425a8f0c2aefdb53bf8e82867801dc1bd4929442a'
            'abbac0667f15870da50e19601bec90b4a3323e38e8d99bc2340037dff5091658'
            '5ae30f0101c5ce031c2a22531b099e16b1796bca1ef640dde087f0caaf34265d'
            'd89423836be0cb5ca076e173ea373c4deeef3d6ffa17085ca8a0850b364d7d3b'
            '933c61f15a81ac9c50f66f8c6c059d09f94a116d7b4c4d534a41b1c8f0140160')
validpgpkeys=(
	'8657ABB260F056B1E5190839D9C4D26D0E604491'
	'7953AC1FBC3DC8B3B292393ED5E9E43F7DF9EE8C'
	'A21FAB74B0088AA361152586B8EF1A6BA9DA2D5C'
	'EFC0A467D613CB83C7ED6D30D894E2CE8B3D79F5'
)

prepare() {
	cd "$srcdir/$_pkgname-$_ver"

	# Files created by the patches
	rm -f \
		include/internal/unicode.h \
		test/recipes/70-test_npn.t \
		test/recipes/80-test_pkcs12_data/bad{1,2,3}.p12 \
		util/perl/TLSProxy/NextProto.pm \
		;

	# set ca dir to /etc/ssl by default
	patch -p0 -i "$srcdir/ca-dir.patch"

	patch -p1 -i "${srcdir}/CVE-2023-5678.patch"
	patch -p1 -i "${srcdir}/CVE-2024-0727-1.patch"
	patch -p1 -i "${srcdir}/CVE-2024-0727-2.patch"
	patch -p1 -i "${srcdir}/CVE-2024-2511.patch"
	patch -p1 -i "${srcdir}/CVE-2024-4741.patch"
	patch -p1 -i "${srcdir}/CVE-2024-5535-1.patch"
	patch -p1 -i "${srcdir}/CVE-2024-5535-2.patch"
	patch -p1 -i "${srcdir}/CVE-2024-5535-3.patch"
	patch -p1 -i "${srcdir}/CVE-2024-5535-4.patch"
	patch -p1 -i "${srcdir}/CVE-2024-5535-5.patch"
	patch -p1 -i "${srcdir}/CVE-2024-5535-6.patch"
	patch -p1 -i "${srcdir}/CVE-2024-5535-7.patch"
	patch -p1 -i "${srcdir}/CVE-2024-5535-8.patch"
	patch -p1 -i "${srcdir}/CVE-2024-9143.patch"
	patch -p1 -i "${srcdir}/CVE-2024-13176.patch"
	patch -p1 -i "${srcdir}/CVE-2025-9230.patch"
	patch -p1 -i "${srcdir}/CVE-2025-68160.patch"
	patch -p1 -i "${srcdir}/CVE-2025-69418.patch"
	patch -p1 -i "${srcdir}/CVE-2025-69419-1.patch"
	patch -p1 -i "${srcdir}/CVE-2025-69419-2.patch"
	patch -p1 -i "${srcdir}/CVE-2025-69420.patch"
	patch -p1 -i "${srcdir}/CVE-2025-69421.patch"
	patch -p1 -i "${srcdir}/CVE-2026-22795_CVE-2026-22796.patch"
}

build() {
	cd "$srcdir/$_pkgname-$_ver"

	./Configure --prefix=/usr --openssldir=/etc/ssl --libdir=lib/openssl-1.1 \
		shared no-ssl3-method enable-ec_nistp_64_gcc_128 "linux-${CARCH}"

	make depend
	make
}

check() {
	cd "$srcdir/$_pkgname-$_ver"

	# the test fails due to missing write permissions in /etc/ssl
	# revert this patch for make test
	patch -p0 -R -i "$srcdir/ca-dir.patch"

	make test

	patch -p0 -i "$srcdir/ca-dir.patch"
	# re-run make to re-generate CA.pl from th patched .in file.
	make apps/CA.pl
}

package() {
	cd "$srcdir/$_pkgname-$_ver"

	make DESTDIR="$pkgdir" install_sw

	# Move some files around
	install -m755 -d "$pkgdir/usr/include/openssl-1.1"
	mv "$pkgdir/usr/include/openssl" "$pkgdir/usr/include/openssl-1.1/"
	mv "$pkgdir/usr/lib/openssl-1.1/libcrypto.so.1.1" "$pkgdir/usr/lib/"
	mv "$pkgdir/usr/lib/openssl-1.1/libssl.so.1.1" "$pkgdir/usr/lib/"
	ln -sf ../libssl.so.1.1 "$pkgdir/usr/lib/openssl-1.1/libssl.so"
	ln -sf ../libcrypto.so.1.1 "$pkgdir/usr/lib/openssl-1.1/libcrypto.so"
	mv "$pkgdir/usr/bin/openssl" "$pkgdir/usr/bin/openssl-1.1"

	# Update includedir in .pc files
	sed -e 's|/include$|/include/openssl-1.1|' -i "$pkgdir"/usr/lib/openssl-1.1/pkgconfig/*.pc

	rm -rf "$pkgdir"/{etc,usr/bin/c_rehash}

	install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
