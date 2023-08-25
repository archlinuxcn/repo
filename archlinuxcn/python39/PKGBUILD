# Maintainer: Tobias Kunze <r@rixx.de>
# Maintained at https://github.com/rixx/pkgbuilds, feel free to submit patches

pkgname=python39
pkgver=3.9.18
pkgrel=1
_pybasever=3.9
_pymajver=3
pkgdesc="Major release 3.9 of the Python high-level programming language"
arch=('i686' 'x86_64')
license=('custom')
url="https://www.python.org/"
depends=('bzip2' 'expat' 'gdbm' 'libffi' 'libnsl' 'libxcrypt' 'openssl' 'zlib')
makedepends=('bluez-libs' 'mpdecimal' 'gdb' 'tk')
optdepends=('sqlite' 'mpdecimal: for decimal' 'xz: for lzma' 'tk: for tkinter')
source=(
    https://www.python.org/ftp/python/${pkgver}/Python-${pkgver}.tar.xz
    mpdecimal-2.5.1.patch
)
sha256sums=(
    '01597db0132c1cf7b331eff68ae09b5a235a3c3caa9c944c29cac7d1c4c4c00a'
    '8eb389be1babe03a0231001dc16dd2d69a3ea0fbf6b8c976a580787e7ff1594c'
)
validpgpkeys=(
    '0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D'  # Ned Deily (Python release signing key) <nad@python.org>
    'E3FF2839C048B25C084DEBE9B26995E310250568'  # Łukasz Langa (GPG langa.pl) <lukasz@langa.pl>
)
provides=("python=$pkgver")

prepare() {
  cd "${srcdir}/Python-${pkgver}"

  patch -p1 -i "${srcdir}/mpdecimal-2.5.1.patch"

  # FS#23997
  sed -i -e "s|^#.* /usr/local/bin/python|#!/usr/bin/python|" Lib/cgi.py

  # Ensure that we are using the system copy of various libraries (expat, zlib and libffi),
  # rather than copies shipped in the tarball
  rm -rf Modules/expat
  rm -rf Modules/zlib
  rm -rf Modules/_ctypes/{darwin,libffi}*
  rm -rf Modules/_decimal/libmpdec
}

build() {
  cd "${srcdir}/Python-${pkgver}"
  CFLAGS="${CFLAGS} -fno-semantic-interposition"

  export ax_cv_c_float_words_bigendian=no
  ./configure --prefix=/usr \
              --enable-shared \
              --with-computed-gotos \
              --with-lto \
              --enable-ipv6 \
              --with-system-expat \
              --with-dbmliborder=gdbm:ndbm \
              --with-system-ffi \
              --with-system-libmpdec \
              --enable-loadable-sqlite-extensions \
              --without-ensurepip \
              --with-tzpath=/usr/share/zoneinfo

  make EXTRA_CFLAGS="$CFLAGS"
}

package() {
  cd "${srcdir}/Python-${pkgver}"
  # altinstall: /usr/bin/pythonX.Y but not /usr/bin/python or /usr/bin/pythonX
  make DESTDIR="${pkgdir}" altinstall maninstall

  # Split tests
  rm -r "$pkgdir"/usr/lib/python*/{test,ctypes/test,distutils/tests,idlelib/idle_test,lib2to3/tests,sqlite3/test,tkinter/test,unittest/test}

  # Avoid conflicts with the main 'python' package.
  rm -f "${pkgdir}/usr/lib/libpython${_pymajver}.so"
  rm -f "${pkgdir}/usr/share/man/man1/python${_pymajver}.1"

  # Clean-up reference to build directory
  sed -i "s|$srcdir/Python-${pkgver}:||" "$pkgdir/usr/lib/python${_pybasever}/config-${_pybasever}-${CARCH}-linux-gnu/Makefile"

  # Add useful scripts FS#46146
  install -dm755 "${pkgdir}"/usr/lib/python${_pybasever}/Tools/{i18n,scripts}
  install -m755 Tools/i18n/{msgfmt,pygettext}.py "${pkgdir}"/usr/lib/python${_pybasever}/Tools/i18n/
  install -m755 Tools/scripts/{README,*py} "${pkgdir}"/usr/lib/python${_pybasever}/Tools/scripts/

  # License
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
