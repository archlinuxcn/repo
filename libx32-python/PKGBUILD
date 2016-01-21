# $Id: PKGBUILD 255786 2015-12-11 07:23:13Z fyan $
# Maintainer: Angel Velasquez <angvp@archlinux.org>
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Jason Chu <jason@archlinux.org>
# x23 Maintainer: Fantix King <fantix.king@gmail.com>

_pkgbasename=python
pkgname=libx32-python
pkgver=3.5.1
pkgrel=1.2
_pybasever=3.5
pkgdesc="Next generation of the python high-level scripting language (x32 ABI)"
arch=('x86_64')
license=('custom')
url="http://www.python.org/"
depends=('libx32-expat' 'libx32-bzip2' 'libx32-gdbm' 'libx32-openssl' 'libx32-libffi' 'libx32-zlib' $_pkgbasename)
makedepends=('libx32-tk' 'libx32-sqlite' 'bluez-libs' 'libx32-mpdecimal' 'libx32-readline' 'libx32-xz')
checkdepends=('gdb' 'xorg-server-xvfb')
optdepends=('libx32-sqlite'
            'libx32-readline'
            'libx32-ncurses: for curses'
            'libx32-mpdecimal: for decimal'
            'libx32-xz: for lzma'
            'libx32-tk: for tkinter')
options=('!makeflags')
source=("http://www.python.org/ftp/python/${pkgver%rc*}/Python-${pkgver}.tar.xz"
        pyconfig-stub.h
        venv-x32.patch
        site.py.patch
        dont-make-libpython-readonly.patch)
sha1sums=('0186da436db76776196612b98bb9c2f76acfe90e'
          '74e5b55b394b1dfe5c430734e2ce049d595fb50f'
          'af6b854349f4992892471b9cb363e8a6ce19ea6b'
          'f0fe25082c2b080dccf19400fe998d97f3adf5a4'
          'c22b24324b8e53326702de439c401d97927ee3f2')

prepare() {
  cd Python-${pkgver}

  # FS#45809
  patch -p1 -i ../dont-make-libpython-readonly.patch

  # x32 venv
  patch -p1 -i ../venv-x32.patch

  # site.py
  patch -p1 -i ../site.py.patch

  # FS#23997
  sed -i -e "s|^#.* /usr/local/bin/python|#!/usr/bin/python-x32|" Lib/cgi.py

  # Ensure that we are using the system copy of various libraries (expat, zlib, libffi, and libmpdec),
  # rather than copies shipped in the tarball
  rm -r Modules/expat
  rm -r Modules/zlib
  rm -r Modules/_ctypes/{darwin,libffi}*
  rm -r Modules/_decimal/libmpdec

  # x32 fixes
  sed -i "s|base}/lib|base}/libx32|g" "${srcdir}/Python-${pkgver}/Lib/sysconfig.py"
  sed -i "s|/include|/libx32/python{py_version_short}/include|g" "${srcdir}/Python-${pkgver}/Lib/sysconfig.py"
  sed -i "s|lib/|libx32/|g" "${srcdir}/Python-${pkgver}/Modules/getpath.c"
  sed -i "s|base/lib|base/libx32|g" "${srcdir}/Python-${pkgver}/Lib/distutils/command/install.py"
  sed -i "s|/include|/libx32/python$py_version_short/include|g" "${srcdir}/Python-${pkgver}/Lib/distutils/command/install.py"
  sed -i "s|prefix)/lib|prefix)/libx32|g" "${srcdir}/Python-${pkgver}/Makefile.pre.in"
  sed -i "s|lib/python|libx32/python|g" "${srcdir}/Python-${pkgver}/configure"
  sed -i "s|\"lib\"|\"libx32\"|g" "${srcdir}/Python-${pkgver}/Lib/distutils/sysconfig.py"
}

build() {
  cd Python-${pkgver}

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export LDFLAGS='-mx32'
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"
  export OPT="${CFLAGS}"

  # Disable bundled pip & setuptools
  ./configure --prefix=/usr \
              --libdir=/usr/libx32 \
              --with-suffix='-x32' \
              --enable-shared \
              --with-threads \
              --with-computed-gotos \
              --enable-ipv6 \
              --with-system-expat \
              --with-dbmliborder=gdbm:ndbm \
              --with-system-ffi \
              --with-system-libmpdec \
              --enable-loadable-sqlite-extensions \
              --without-ensurepip

  make EXTRA_CFLAGS="$CFLAGS"
}

check() {
  # Failures:
  # test_pathlib & test_posixpath: https://bugs.python.org/issue24950
  # test_gdb
  # test_distutils: because of our EXTRA_CFLAGS
  # test_nntplib: downloading external files and failed

  # Hacks:
  # test_tk: xvfb-run
  # test_unicode_file: LC_CTYPE=en_US.utf-8
  # test_gdb: SHELL=/bin/sh

  cd Python-${pkgver}
  SHELL=/bin/sh \
  LD_LIBRARY_PATH="${srcdir}/Python-${pkgver}":${LD_LIBRARY_PATH} \
  LC_CTYPE=en_US.utf-8 xvfb-run \
    "${srcdir}/Python-${pkgver}/python-x32" -m test.regrtest -v -uall || warning "Expected failure"
}

package() {
  install="${pkgname}.install"

  cd Python-${pkgver}
  make DESTDIR="${pkgdir}" EXTRA_CFLAGS="$CFLAGS" install maninstall

  # Why are these not done by default...
  ln -s python3-x32               "${pkgdir}"/usr/bin/python-x32
  ln -s python3-x32-config        "${pkgdir}"/usr/bin/python-x32-config
  ln -s idle3-x32                 "${pkgdir}"/usr/bin/idle-x32

  # Fix FS#22552
  ln -sf ../../libpython${_pybasever}m.so \
    "${pkgdir}/usr/libx32/python${_pybasever}/config-${_pybasever}m/libpython${_pybasever}m.so"

  # some useful "stuff" FS#46146
  install -dm755 "${pkgdir}"/usr/libx32/python${_pybasever}/Tools/{i18n,scripts}
  install -m755 Tools/i18n/{msgfmt,pygettext}.py "${pkgdir}"/usr/libx32/python${_pybasever}/Tools/i18n/
  install -m755 Tools/scripts/{README,*py} "${pkgdir}"/usr/libx32/python${_pybasever}/Tools/scripts/

  # Clean-up reference to build directory
  sed -i "s|$srcdir/Python-${pkgver}:||" "$pkgdir/usr/libx32/python${_pybasever}/config-${_pybasever}m/Makefile"

  mv "${pkgdir}/usr/include/python3.5m/pyconfig.h" "${srcdir}/pyconfig-x32.h"
  rm -rf "${pkgdir}"/usr/{include,share}
  mkdir -p "$pkgdir/usr/include/python3.5m"
  install -Dm644 "${srcdir}/pyconfig-x32.h" "${pkgdir}/usr/include/python3.5m/pyconfig-x32.h"
  install -Dm644 "${srcdir}/pyconfig-stub.h" "${pkgdir}/usr/include/python3.5m/pyconfig-stub.h"

  rm "${pkgdir}"/usr/bin/2to3{,-3.5}
  rm "${pkgdir}"/usr/bin/idle3
  mv "${pkgdir}"/usr/bin/idle3.5{,-x32}
  ln -s idle3.5-x32 "${pkgdir}"/usr/bin/idle3-x32
  rm "${pkgdir}"/usr/bin/pydoc3{,.5}
  rm "${pkgdir}"/usr/bin/python3{,.5}-config
  mv "${pkgdir}"/usr/bin/python3.5m{,-x32}-config
  ln -s python3.5m-x32-config "${pkgdir}"/usr/bin/python3.5-x32-config
  ln -s python3.5-x32-config "${pkgdir}"/usr/bin/python3-x32-config
  rm "${pkgdir}"/usr/bin/pyvenv
  mv "${pkgdir}"/usr/bin/pyvenv-3.5{,-x32}
  ln -s pyvenv-3.5-x32 "${pkgdir}"/usr/bin/pyvenv-x32

  # License
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
