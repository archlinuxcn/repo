# Maintainer: Kevin Brodsky <corax26 at gmail dot com>

_pkgbasename=ncurses
pkgname=lib32-${_pkgbasename}5-compat-libs
_pkgver=6.0-20170527
pkgver=${_pkgver/-/+}
pkgrel=1
pkgdesc="System V Release 4.0 curses emulation library (32-bit), ABI 5"
arch=('x86_64')
url='http://invisible-island.net/ncurses/ncurses.html'
license=('MIT')
depends=('lib32-glibc' "lib32-${_pkgbasename}")
makedepends=("gcc-multilib")
# Temporary URL, the upstream invisible-island URL will be used again when the
# core ncurses package is updated to a more recent version.
source=(https://www.mirrorservice.org/sites/lynx.isc.org/ncurses/current/ncurses-${_pkgver}.tgz{,.asc})
md5sums=('c0e32e50ed6fd81af7ecc4910de9fa3f'
         'SKIP')
validpgpkeys=('C52048C0C0748FEE227D47A2702353E0F7E48EDB') # Thomas Dickey

build() {
  cd ${_pkgbasename}-${_pkgver}

  export CC="gcc -m32"
  export CXX="g++ -m32"

  ./configure --prefix=/usr --mandir=/usr/share/man \
     --with-shared --with-normal --without-debug --without-ada \
     --with-install-prefix=${pkgdir} --enable-widec --libdir=/usr/lib32 \
     --with-abi-version=5 --without-pkg-config --without-gpm
   make
}

package() {
  cd ${_pkgbasename}-${_pkgver}
  make install.libs

  install -dm755 ${pkgdir}/usr/lib32

  # fool packages looking to link to non-wide-character ncurses libraries
  for lib in ncurses form panel menu; do
    ln -s lib${lib}w.so.5 "$pkgdir"/usr/lib32/lib${lib}.so.5
  done
  # Also provide a libtinfo symlink
  ln -s libncurses.so.5 "$pkgdir/usr/lib32/libtinfo.so.5"

  # Remove .so symlinks and static libraries (conflicting with lib32-ncurses)
  rm -f "${pkgdir}"/usr/{lib32/*.so,lib32/*.a}

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}

# vim: set et ts=2 sw=2:
