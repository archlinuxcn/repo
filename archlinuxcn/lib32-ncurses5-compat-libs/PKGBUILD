# Maintainer: Kevin Brodsky <corax26 at gmail dot com>

_pkgbasename=ncurses
pkgname=lib32-${_pkgbasename}5-compat-libs
pkgver=6.2
pkgrel=1
pkgdesc="System V Release 4.0 curses emulation library (32-bit), ABI 5"
arch=('x86_64')
url="https://www.gnu.org/software/ncurses/"
license=('MIT')
depends=('lib32-glibc' "lib32-${_pkgbasename}")
source=(https://ftp.gnu.org/pub/gnu/ncurses/ncurses-$pkgver.tar.gz{,.sig})
sha512sums=('4c1333dcc30e858e8a9525d4b9aefb60000cfc727bc4a1062bace06ffc4639ad9f6e54f6bdda0e3a0e5ea14de995f96b52b3327d9ec633608792c99a1e8d840d'
            'SKIP')
validpgpkeys=('C52048C0C0748FEE227D47A2702353E0F7E48EDB') # Thomas Dickey

build() {
  cd ${_pkgbasename}-${pkgver}

  export CC="gcc -m32"
  export CXX="g++ -m32"

  ./configure --prefix=/usr --mandir=/usr/share/man \
     --with-shared --with-normal --without-debug --without-ada \
     --enable-widec --libdir=/usr/lib32 \
     --with-abi-version=5 --without-pkg-config --without-gpm \
     --with-versioned-syms
   make
}

package() {
  cd ${_pkgbasename}-${pkgver}
  make DESTDIR="${pkgdir}" install.libs

  # fool packages looking to link to non-wide-character ncurses libraries
  for lib in ncurses form panel menu; do
    ln -s lib${lib}w.so.5 "$pkgdir"/usr/lib32/lib${lib}.so.5
  done

  for lib in tic tinfo; do
    ln -s libncursesw.so.5 "${pkgdir}/usr/lib32/lib${lib}.so.5"
   done

  # Remove .so symlinks and static libraries (conflicting with lib32-ncurses)
  rm -f "${pkgdir}"/usr/{lib32/*.so,lib32/*.a}

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}

# vim: set et ts=2 sw=2:
