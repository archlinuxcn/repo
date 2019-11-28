# Maintainer: Daniel Milde <daniel@milde.cz>
# Co-Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Modified from extra/python; original contributors:
# Contributor: Angel Velasquez <angvp@archlinux.org>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Jason Chu <jason@archlinux.org>

pkgname=python-git
pkgver=3.9.0a0.r105882.2582d46fbcf
pkgrel=1
_pybasever=3.9
pkgdesc="Next generation of the python high-level scripting language"
arch=('x86_64')
license=('custom')
url="https://www.python.org/"
depends=('expat' 'bzip2' 'gdbm' 'openssl' 'libffi' 'zlib' 'libnsl')
makedepends=('tk' 'sqlite' 'valgrind' 'bluez-libs' 'mpdecimal' 'xz' 'git' 'llvm' 'gdb' 'xorg-server-xvfb')
checkdepends=('ttf-font')
optdepends=('sqlite'
            'mpdecimal: for decimal'
            'xz: for lzma'
            'tk: for tkinter')
source=("git+https://github.com/python/cpython#branch=master"
        $pkgname-issue38692.diff)
sha512sums=('SKIP'
            'bb18f476e74d969a16aa4077f01963f551b067d5dbeae80159d663dcf4f8e043f446c4c888388fbe3436d31d29401f6cbcfc74ace9257879e32b0d7731245a47')

pkgver() {
  cd cpython
  printf "%s.r%s.%s" \
      "$_pybasever.0a0" \
      "$(git rev-list --count HEAD)" \
      "$(git rev-parse --short HEAD)"
}

prepare() {
  cd cpython

  # https://bugs.python.org/issue38692
  patch -Np1 -i ../$pkgname-issue38692.diff

  # FS#23997
  sed -i -e "s|^#.* /usr/local/bin/python|#!/usr/bin/python|" Lib/cgi.py

  # Speed up LTO
  sed -i -e "s|-flto |-flto=4 |g" configure configure.ac

  # Ensure that we are using the system copy of various libraries (expat, libffi, and libmpdec),
  # rather than copies shipped in the tarball
  rm -r Modules/expat
  rm -r Modules/_ctypes/{darwin,libffi}*
  rm -r Modules/_decimal/libmpdec
}

build() {
  cd cpython

  # PGO should be done with -O3
  CFLAGS="${CFLAGS/-O2/-O3}"

  ./configure --prefix=/usr \
              --enable-shared \
              --with-threads \
              --with-computed-gotos \
              --enable-optimizations \
              --with-lto \
              --enable-ipv6 \
              --with-system-expat \
              --with-dbmliborder=gdbm:ndbm \
              --with-system-ffi \
              --with-system-libmpdec \
              --enable-loadable-sqlite-extensions

  # Obtain next free server number for xvfb-run; this even works in a chroot environment.
  export servernum=99
  while ! xvfb-run -a -n "$servernum" /bin/true 2>/dev/null; do servernum=$((servernum+1)); done

  LC_CTYPE=en_US.UTF-8 xvfb-run -s "-screen 0 1280x720x24 -ac +extension GLX" -a -n "$servernum" make EXTRA_CFLAGS="$CFLAGS"
}

check() {
  # test_ttk_guionly hangs under certain circumstances
  # test_tk failed since tcl-& tk 8.6.10

  cd cpython

  # Obtain next free server number for xvfb-run; this even works in a chroot environment.
  export servernum=99
  while ! xvfb-run -a -n "$servernum" /bin/true 2>/dev/null; do servernum=$((servernum+1)); done

  LD_LIBRARY_PATH="${srcdir}/cpython":${LD_LIBRARY_PATH} \
  LC_CTYPE=en_US.UTF-8 xvfb-run -s "-screen 0 1280x720x24 -ac +extension GLX" -a -n "$servernum" \
    "${srcdir}/cpython/python" -m test.regrtest -w -uall -x test_ttk_guionly -x test_tk -j -1
}

package() {
  cd cpython

  # Hack to avoid building again
  sed -i 's/^all:.*$/all: build_all/' Makefile

  # PGO should be done with -O3
  CFLAGS="${CFLAGS/-O2/-O3}"

  make DESTDIR="${pkgdir}" EXTRA_CFLAGS="$CFLAGS" ENSUREPIP=install altinstall maninstall

  # Work around a conflict with the 'python' package.
  rm "${pkgdir}/usr/lib/libpython3.so"
  rm "${pkgdir}/usr/share/man/man1/python3.1"

  # some useful "stuff" FS#46146
  install -dm755 "${pkgdir}"/usr/lib/python${_pybasever}/Tools/{i18n,scripts}
  install -m755 Tools/i18n/{msgfmt,pygettext}.py "${pkgdir}"/usr/lib/python${_pybasever}/Tools/i18n/
  install -m755 Tools/scripts/{README,*py} "${pkgdir}"/usr/lib/python${_pybasever}/Tools/scripts/

  # License
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
