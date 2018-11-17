pkgname=python36
pkgver=3.6.7
pkgrel=1
_pybasever=3.6
_pymajver=3
pkgdesc="Major release 3.6 of the Python high-level programming language"
arch=('i686' 'x86_64')
license=('custom')
url="http://www.python.org/"
depends=('expat' 'bzip2' 'gdbm' 'openssl' 'libffi' 'zlib')
makedepends=('tk' 'sqlite' 'bluez-libs' 'mpdecimal')
optdepends=('tk: for tkinter' 'sqlite')
options=('!makeflags')
source=(http://www.python.org/ftp/python/${pkgver}/Python-${pkgver}.tar.xz)
sha256sums=('81fd1401a9d66533b0a3e9e3f4ea1c7c6702d57d5b90d659f971e6f1b745f77d')
# Maintainer: Tobias Kunze <r@rixx.de>
# Based on python33 script from: Rodolphe Breard <packages@what.tf> and Christopher Arndt <chris@chrisarndt.de>
# Via the python34 adaption of Raphael Michel <mail@raphaelmichel.de>

prepare() {
  cd "${srcdir}/Python-${pkgver}"

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

  CFLAGS=-DOPENSSL_NO_SSL2 ./configure --prefix=/usr \
              --enable-shared \
              --with-threads \
              --with-computed-gotos \
              --enable-ipv6 \
              --with-system-expat \
              --with-dbmliborder=gdbm:ndbm \
              --with-system-libmpdec \
              --enable-loadable-sqlite-extensions \
              --without-ensurepip

  make
}

package() {
  cd "${srcdir}/Python-${pkgver}"
  # altinstall: /usr/bin/pythonX.Y but not /usr/bin/python or /usr/bin/pythonX
  make DESTDIR="${pkgdir}" altinstall maninstall

  # Avoid conflicts with the main 'python' package, once Python 3.7 is standard.
  rm "${pkgdir}/usr/lib/libpython${_pymajver}.so"
  rm "${pkgdir}/usr/share/man/man1/python${_pymajver}.1"

  # Fix FS#22552
  ln -sf ../../libpython${_pybasever}m.so \
    "${pkgdir}/usr/lib/python${_pybasever}/config-${_pybasever}m-${CARCH}-linux-gnu/libpython${_pybasever}m.so"

  # Fix pycairo build
  ln -sf python${_pybasever}m-config "${pkgdir}/usr/bin/python${_pybasever}-config"

  # Clean-up reference to build directory
  sed -i "s|$srcdir/Python-${pkgver}:||" "$pkgdir/usr/lib/python${_pybasever}/config-${_pybasever}m-${CARCH}-linux-gnu/Makefile"

  # License
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
