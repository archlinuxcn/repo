# Maintainer: Heptazhou <zhou at 0h7z dot com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Frederik Schwan <freswa at archlinux dot org>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->glibc->binutils->gcc
# NOTE: valgrind requires rebuilt with each major glibc version

pkgbase=glibc-linux4
pkgname=(glibc-linux4 lib32-glibc-linux4)
pkgver_=c804cd1c00adde061ca51711f63068c103e94eef
pkgver=2.36
pkgrel=1
arch=(x86_64)
url="https://www.gnu.org/software/libc/"
license=(GPL LGPL)
makedepends=(git gd lib32-gcc-libs python)
options=(debug staticlibs !lto)
source=(
	# git+https://sourceware.org/git/glibc.git#commit=$pkgver_
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
	# "SKIP"
	"1c959fea240906226062cb4b1e7ebce71a9f0e3c0836c09e7e3423d434fcfe75" "SKIP"
	"69573c1c4eee6216f4f345647aed938d13994bf19a7e3a6ba9ed8bab85f23bef"
	"fbd57987ca24d71305eda9e0dd76143b422118e12f76b2b0d555f86763e14cd2"
	"7503947e23cecc8307e8f7ce2a792eecb6f72f22d6838b34417c2489a259fde9"
	"c27424154a6096ae32c0824b785e05de6acef33d9224fd6147d1936be9b4962b"
	"774061aff612a377714a509918a9e0e0aafce708b87d2d7e06b1bd1f6542fe70"
	"cdc234959c6fdb43f000d3bb7d1080b0103f4080f5e67bcfe8ae1aaf477812f0"
)

prepare() {
	mkdir -p glibc-build lib32-glibc-build

	[[ -d glibc-$pkgver ]] && ln -s glibc-$pkgver glibc
	cd glibc

	# compatibility with linux 4.x hosts
	# patch -Np1 < "$srcdir"/glibc-linux4.patch
}

build() {
	local _configure_flags=(
		--prefix=/usr
		--with-headers=/usr/include
		--with-bugurl=https://bugs.archlinux.org/
		--enable-bind-now
		--enable-cet
		--enable-kernel=4.4.0
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

	# Credits @allanmcrae
	# https://github.com/allanmcrae/toolchain/blob/f18604d70c5933c31b51a320978711e4e6791cf1/glibc/PKGBUILD
	# remove fortify for building libraries
	CFLAGS=${CFLAGS/-Wp,-D_FORTIFY_SOURCE=2/}

	"$srcdir/glibc/configure" \
		--libdir=/usr/lib \
		--libexecdir=/usr/lib \
		"${_configure_flags[@]}"

	# build libraries with fortify disabled
	echo "build-programs=no" >> configparms
	make -O

	# re-enable fortify for programs
	sed -i "/build-programs=/s#no#yes#" configparms
	echo "CFLAGS += -Wp,-D_FORTIFY_SOURCE=2" >> configparms
	make -O

	# build info pages manually for reproducibility
	make info

	cd -- "$srcdir/lib32-glibc-build"
	export CC="gcc -m32 -mstackrealign"
	export CXX="g++ -m32 -mstackrealign"

	echo "slibdir=/usr/lib32" >> configparms
	echo "rtlddir=/usr/lib32" >> configparms
	echo "sbindir=/usr/bin" >> configparms
	echo "rootsbindir=/usr/bin" >> configparms

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
	echo "CFLAGS += -Wp,-D_FORTIFY_SOURCE=2" >> configparms
	make -O

	# pregenerate C.UTF-8 locale until it is built into glibc
	# (https://sourceware.org/glibc/wiki/Proposals/C.UTF-8, FS#74864)
	locale/localedef -c -f ../glibc/localedata/charmaps/UTF-8 -i ../glibc/localedata/locales/C ../C.UTF-8/ \
		|| localedef -c -f ../glibc/localedata/charmaps/UTF-8 -i ../glibc/localedata/locales/C ../C.UTF-8/ \
		|| true
}

check() {
	cd glibc-build

	# adjust/remove buildflags that cause false-positive testsuite failures
	sed -i '/FORTIFY/d' configparms # failure to build testsuite
	sed -i 's/-Werror=format-security/-Wformat-security/' config.make # failure to build testsuite
	sed -i '/CFLAGS/s/-fno-plt//' config.make # 16 failures
	sed -i '/CFLAGS/s/-fexceptions//' config.make # 1 failure
	LDFLAGS=${LDFLAGS/,-z,now/} # 10 failures

	# some failures are "expected"
	# make -O check || \ #
	true
}

package_glibc-linux4() {
	pkgdesc="GNU C Library (linux 4.x compat)"
	depends=("linux-api-headers>=4.10" tzdata filesystem)
	provides=("glibc=$pkgver")
	conflicts=("glibc")
	optdepends=("gd: for memusagestat" "perl: for mtrace")
	install=glibc.install
	backup=(
		etc/gai.conf
		etc/locale.gen
		etc/nscd.conf
	)

	make -C glibc-build install_root="$pkgdir" install
	rm -f "$pkgdir"/etc/ld.so.cache

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

	if [[ -f "$srcdir/C.UTF-8" ]]; then
		# install C.UTF-8 so that it is always available
		install -dm755 "$pkgdir/usr/lib/locale"
		cp -r "$srcdir/C.UTF-8" -t "$pkgdir/usr/lib/locale"
		sed -i '/#C\.UTF-8 /d' "$pkgdir/etc/locale.gen"
	fi

	# Provide tracing probes to libstdc++ for exceptions, possibly for other
	# libraries too. Useful for gdb's catch command.
	install -Dm644 "$srcdir/sdt.h" "$pkgdir/usr/include/sys/sdt.h"
	install -Dm644 "$srcdir/sdt-config.h" "$pkgdir/usr/include/sys/sdt-config.h"
}

package_lib32-glibc-linux4() {
	pkgdesc="GNU C Library (linux 4.x compat, 32-bit)"
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
}
