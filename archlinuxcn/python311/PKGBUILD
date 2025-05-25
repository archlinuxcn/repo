# Maintainer: Heptazhou <zhou at 0h7z dot com>
# Contributor: morwel
# Contributor: Angel Velasquez <angvp@archlinux.org>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Jason Chu <jason@archlinux.org>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=python311
pkgver=3.11.11
pkgrel=3
_pybasever=${pkgver%.*}
pkgdesc="The Python programming language (version 3.11)"
arch=("x86_64")
license=("PSF-2.0")
url="https://www.python.org/"
depends=("mpdecimal")
makedepends=("gdb")
optdepends=("python-pip" "python-pipx" "python-setuptools" "tk")
options=(strip !debug !lto)
source=(
	https://www.python.org/ftp/python/${pkgver%rc*}/Python-${pkgver}.tar.xz #{,.asc}
	EXTERNALLY-MANAGED
)
sha256sums=(
	"2a9920c7a0cd236de33644ed980a13cbbc21058bfdc528febb6081575ed73be3" # "SKIP"
	"d96bca8f7be0d1a83eb88f7c40924434168b1cb8a57870a55ad34207a3718c0a"
)
validpgpkeys=(
	"0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D" # Ned Deily (Python release signing key) <nad@python.org>
	"E3FF2839C048B25C084DEBE9B26995E310250568" # Łukasz Langa (GPG langa.pl) <lukasz@langa.pl>
	"A035C8C19219BA821ECEA86B64E628F8D684696D" # Pablo Galindo Salgado <pablogsal@gmail.com>
)

prepare() {
	cd Python-${pkgver}

	# FS#23997
	sed -i -e "s|^#.* /usr/local/bin/python|#!/usr/bin/python|" Lib/cgi.py

	# Ensure that we are using the system copy of various libraries (expat, libffi, and libmpdec),
	# rather than copies shipped in the tarball
	rm -r Modules/expat
	rm -r Modules/_ctypes/{darwin,libffi}*
	rm -r Modules/_decimal/libmpdec
}

build() {
	cd Python-${pkgver}

	# PGO should be done with -O3
	CFLAGS="${CFLAGS/-O2/-O3} -ffat-lto-objects"

	# Disable bundled pip & setuptools
	./configure \
		ax_cv_c_float_words_bigendian=no \
		--prefix=/usr \
		--enable-shared \
		--with-computed-gotos \
		--enable-optimizations \
		--with-lto=no \
		--enable-ipv6 \
		--with-system-expat \
		--with-dbmliborder=gdbm:ndbm \
		--with-system-libmpdec \
		--enable-loadable-sqlite-extensions \
		--without-ensurepip \
		--with-tzpath=/usr/share/zoneinfo

	make EXTRA_CFLAGS="$CFLAGS"
}

package() {
	cd Python-${pkgver}

	# Hack to avoid building again
	sed -i 's/^all:.*$/all: build_all/' Makefile

	# PGO should be done with -O3
	CFLAGS="${CFLAGS/-O2/-O3}"

	make DESTDIR="${pkgdir}" EXTRA_CFLAGS="$CFLAGS" altinstall maninstall

	# Why are these not done by default...
	# ln -s python3               "${pkgdir}"/usr/bin/python
	# ln -s python3-config        "${pkgdir}"/usr/bin/python-config
	# ln -s idle3                 "${pkgdir}"/usr/bin/idle
	# ln -s pydoc3                "${pkgdir}"/usr/bin/pydoc
	# ln -s python${_pybasever}.1 "${pkgdir}"/usr/share/man/man1/python.1

	# Avoid conflicts with the main "python" package.
	rm -f "${pkgdir}/usr/lib/libpython3.so"
	rm -f "${pkgdir}/usr/share/man/man1/python3.1"

	# Clean-up reference to build directory
	# sed -i "s|$srcdir/Python-${pkgver}||" "$pkgdir/usr/lib/python${_pybasever}/config-${_pybasever}-${CARCH}-linux-gnu/Makefile"

	# some useful "stuff" FS#46146
	install -dm755 "${pkgdir}"/usr/lib/python${_pybasever}/Tools/{i18n,scripts}
	install -m755 Tools/i18n/{msgfmt,pygettext}.py "${pkgdir}"/usr/lib/python${_pybasever}/Tools/i18n/
	install -m755 Tools/scripts/{README,*py} "${pkgdir}"/usr/lib/python${_pybasever}/Tools/scripts/

	# PEP668
	install -Dm644 "$srcdir"/EXTERNALLY-MANAGED -t "${pkgdir}/usr/lib/python${_pybasever}/"

	# Split tests
	cd "$pkgdir"/usr/lib/python*/
	rm -r test && rm -r */*test*/
}
