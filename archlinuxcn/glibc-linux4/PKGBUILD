# Maintainer: Heptazhou <zhou at 0h7z dot com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Frederik Schwan <freswa at archlinux dot org>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->glibc->binutils->gcc
# NOTE: valgrind requires rebuilt with each major glibc version

pkgbase=glibc-linux4
pkgname=(glibc-linux4 lib32-glibc-linux4)
pkgver=2.35
pkgrel=2
arch=(x86_64)
url="https://www.gnu.org/software/libc/"
license=(GPL LGPL)
makedepends=(git gd lib32-gcc-libs python)
optdepends=("perl: for mtrace")
options=(!strip staticlibs !lto)
# _commit=3de512be7ea6053255afed6154db9ee31d4e557a
source=(
	# git+https://sourceware.org/git/glibc.git#commit=$_commit
	https://ftp.gnu.org/gnu/glibc/glibc-$pkgver.tar.xz{,.sig}
	glibc-linux4.patch
	locale.gen.txt
	locale-gen
	lib32-glibc.conf
	sdt.h
	sdt-config.h
)
validpgpkeys=(
	7273542B39962DF7B299931416792B4EA25340F8 # Carlos O'Donell
	BC7C7372637EC10C57D7AA6579C43DFBF1CF2187 # Siddhesh Poyarekar
)
sha256sums=(
	#
	"5123732f6b67ccd319305efd399971d58592122bcc2a6518a1bd2510dd0cf52e" "SKIP"
	"640450afbcb4a0951e56e89d1d8d384e09589032ef32605c08d9894311dda852"
	"fbd57987ca24d71305eda9e0dd76143b422118e12f76b2b0d555f86763e14cd2"
	"83f108f915863c7ed0338e2d3e8f2e071a531a090ef8f8b2eb3a956a3c4f04d7"
	"c27424154a6096ae32c0824b785e05de6acef33d9224fd6147d1936be9b4962b"
	"774061aff612a377714a509918a9e0e0aafce708b87d2d7e06b1bd1f6542fe70"
	"cdc234959c6fdb43f000d3bb7d1080b0103f4080f5e67bcfe8ae1aaf477812f0"
)

prepare() {
	mkdir -p glibc-build lib32-glibc-build

	[[ -d glibc-$pkgver ]] && ln -s glibc-$pkgver glibc
	cd glibc

	# compatibility with linux 4.x hosts
	patch -Np1 < "$srcdir"/glibc-linux4.patch
}

build() {
	local _configure_flags=(
		--prefix=/usr
		--with-headers=/usr/include
		--with-bugurl=https://bugs.archlinux.org/
		--enable-bind-now
		--enable-cet
		--enable-multi-arch
		--enable-stack-protector=strong
		--enable-systemtap
		--disable-profile
		--disable-crypt
		--disable-werror
	)

	cd -- "$srcdir/glibc-build"

	echo "slibdir=/usr/lib" >> configparms
	echo "rtlddir=/usr/lib" >> configparms
	echo "sbindir=/usr/bin" >> configparms
	echo "rootsbindir=/usr/bin" >> configparms

	# remove fortify for building libraries
	CPPFLAGS=${CPPFLAGS/-D_FORTIFY_SOURCE=2/} # Before and
	CFLAGS=${CFLAGS/,-D_FORTIFY_SOURCE=2/} # after https://github.com/archlinux/svntogit-packages/commit/a790c38
	CFLAGS=${CFLAGS/-Wp /}

	#
	CFLAGS=${CFLAGS/-fno-plt/}
	CXXFLAGS=${CXXFLAGS/-fno-plt/}
	LDFLAGS=${LDFLAGS/,-z,now/}

	"$srcdir/glibc/configure" \
		--libdir=/usr/lib \
		--libexecdir=/usr/lib \
		"${_configure_flags[@]}"

	# build libraries with fortify disabled
	echo "build-programs=no" >> configparms
	make -O

	# re-enable fortify for programs
	sed -i "/build-programs=/s#no#yes#" configparms

	echo "CC += -D_FORTIFY_SOURCE=2" >> configparms
	echo "CXX += -D_FORTIFY_SOURCE=2" >> configparms
	make -O

	# build info pages manually for reprducibility
	make info

	cd -- "$srcdir/lib32-glibc-build"
	export CC="gcc -m32 -mstackrealign"
	export CXX="g++ -m32 -mstackrealign"

	echo "slibdir=/usr/lib32" >> configparms
	echo "rtlddir=/usr/lib32" >> configparms
	echo "sbindir=/usr/bin" >> configparms
	echo "rootsbindir=/usr/bin" >> configparms

	# remove fortify for building libraries
	CPPFLAGS=${CPPFLAGS/-D_FORTIFY_SOURCE=2/}
	CFLAGS=${CFLAGS/-fno-plt/}
	CXXFLAGS=${CXXFLAGS/-fno-plt/}

	"$srcdir/glibc/configure" \
		--host=i686-pc-linux-gnu \
		--libdir=/usr/lib32 \
		--libexecdir=/usr/lib32 \
		"${_configure_flags[@]}"

	# build libraries with fortify disabled
	echo "build-programs=no" >> configparms
	make -O

	# re-enable fortify for programs
	sed -i "/build-programs=/s#no#yes#" configparms

	echo "CC += -D_FORTIFY_SOURCE=2" >> configparms
	echo "CXX += -D_FORTIFY_SOURCE=2" >> configparms
	make -O
}

check() {
	cd glibc-build

	# remove fortify in preparation to run test-suite
	sed -i '/FORTIFY/d' configparms

	# some failures are "expected"
	make check || true
}

package_glibc-linux4() {
	pkgdesc="GNU C Library (linux 4.x compat)"
	depends=("linux-api-headers>=4.10" tzdata filesystem)
	provides=("glibc=$pkgver")
	conflicts=("glibc")
	optdepends=("gd: for memusagestat")
	install=glibc.install
	backup=(
		etc/gai.conf
		etc/locale.gen
		etc/nscd.conf
	)

	install -dm755 "$pkgdir/etc"
	touch "$pkgdir/etc/ld.so.conf"

	make -C glibc-build install_root="$pkgdir" install
	rm -f "$pkgdir"/etc/ld.so.{cache,conf}

	# Shipped in tzdata
	rm -f "$pkgdir"/usr/bin/{tzselect,zdump,zic}

	cd glibc

	install -dm755 "$pkgdir"/usr/lib/{locale,systemd/system,tmpfiles.d}
	install -m644 nscd/nscd.conf "$pkgdir/etc/nscd.conf"
	install -m644 nscd/nscd.service "$pkgdir/usr/lib/systemd/system"
	install -m644 nscd/nscd.tmpfiles "$pkgdir/usr/lib/tmpfiles.d/nscd.conf"
	install -dm755 "$pkgdir/var/db/nscd"

	install -m644 posix/gai.conf "$pkgdir"/etc/gai.conf

	install -m755 "$srcdir/locale-gen" "$pkgdir/usr/bin"

	# Create /etc/locale.gen
	install -m644 "$srcdir/locale.gen.txt" "$pkgdir/etc/locale.gen"
	sed -e '1,3d' -e 's|/| |g' -e 's|\\| |g' -e 's|^|#|g' \
		"$srcdir/glibc/localedata/SUPPORTED" >> "$pkgdir/etc/locale.gen"

	if check_option "debug" n; then
		find "$pkgdir"/usr/bin -type f -executable -exec strip $STRIP_BINARIES {} + 2> /dev/null || true
		find "$pkgdir"/usr/lib -name '*.a' -type f -exec strip $STRIP_STATIC {} + 2> /dev/null || true

		# Do not strip these for gdb and valgrind functionality, but strip the rest
		find "$pkgdir"/usr/lib \
			-not -name 'ld-*.so*' \
			-not -name 'libc.so*' \
			-not -name 'libc-*.so' \
			-not -name 'libpthread.so*' \
			-not -name 'libpthread-*.so' \
			-not -name 'libthread_db.so*' \
			-not -name 'libthread_db-*.so' \
			-name '*.so*' -type f -exec strip $STRIP_SHARED {} + 2> /dev/null || true
	fi

	# Provide tracing probes to libstdc++ for exceptions, possibly for other
	# libraries too. Useful for gdb's catch command.
	install -Dm644 "$srcdir/sdt.h" "$pkgdir/usr/include/sys/sdt.h"
	install -Dm644 "$srcdir/sdt-config.h" "$pkgdir/usr/include/sys/sdt-config.h"

	# Provided by libxcrypt; keep the old shared library for backwards compatibility
	rm -f "$pkgdir"/usr/include/crypt.h "$pkgdir"/usr/lib/libcrypt.{a,so}
}

package_lib32-glibc-linux4() {
	pkgdesc="GNU C Library (32-bit, linux 4.x compat)"
	depends=("glibc=$pkgver")
	provides=("lib32-glibc=$pkgver")
	conflicts=("lib32-glibc")
	options+=("!emptydirs")

	cd lib32-glibc-build

	make install_root="$pkgdir" install
	rm -rf "$pkgdir"/{etc,sbin,usr/{bin,sbin,share},var}

	# We need to keep 32 bit specific header files
	find "$pkgdir/usr/include" -type f -not -name '*-32.h' -delete

	# Dynamic linker
	install -d "$pkgdir/usr/lib"
	ln -s ../lib32/ld-linux.so.2 "$pkgdir/usr/lib/"

	# Add lib32 paths to the default library search path
	install -Dm644 "$srcdir/lib32-glibc.conf" "$pkgdir/etc/ld.so.conf.d/lib32-glibc.conf"

	# Symlink /usr/lib32/locale to /usr/lib/locale
	ln -s ../lib/locale "$pkgdir/usr/lib32/locale"

	if check_option "debug" n; then
		find "$pkgdir"/usr/lib32 -name '*.a' -type f -exec strip $STRIP_STATIC {} + 2> /dev/null || true
		find "$pkgdir"/usr/lib32 \
			-not -name 'ld-*.so*' \
			-not -name 'libc.so*' \
			-not -name 'libc-*.so' \
			-not -name 'libpthread.so*' \
			-not -name 'libpthread-*.so' \
			-not -name 'libthread_db.so*' \
			-not -name 'libthread_db-*.so' \
			-name '*.so*' -type f -exec strip $STRIP_SHARED {} + 2> /dev/null || true
	fi

	# Provided by lib32-libxcrypt; keep the old shared library for backwards compatibility
	rm -f "$pkgdir"/usr/lib32/libcrypt.{a,so}
}
