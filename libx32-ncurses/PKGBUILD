# $Id: PKGBUILD 140618 2015-09-17 21:06:06Z foutrelis $
# Maintainer: Allan McRae <allan@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=ncurses
pkgname=libx32-${_pkgbasename}
pkgver=6.0
pkgrel=2.2
pkgdesc="System V Release 4.0 curses emulation library (x32 ABI)"
arch=('x86_64')
url="http://www.gnu.org/software/ncurses/"
license=('MIT')
depends=('libx32-glibc' ${_pkgbasename})
makedepends=("gcc-multilib-x32")
source=(ftp://invisible-island.net/${_pkgbasename}/${_pkgbasename}-${pkgver}.tar.gz{,.asc})
md5sums=('ee13d052e1ead260d7c28071f46eefb1'
         'SKIP')
validpgpkeys=('C52048C0C0748FEE227D47A2702353E0F7E48EDB') # Thomas Dickey

build() {
  cd ${_pkgbasename}-${pkgver}

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./configure --prefix=/usr --mandir=/usr/share/man \
     --with-shared --with-normal --without-debug --without-ada \
     --with-install-prefix=${pkgdir} --enable-widec --libdir=/usr/libx32 \
     --enable-ext-colors --enable-ext-mouse
  make
}

package() {
  cd ${_pkgbasename}-${pkgver}
  make install

  install -dm755 ${pkgdir}/usr/libx32

  # fool packages looking to link to non-wide-character ncurses libraries
  for lib in curses ncurses form panel menu; do
    rm -f ${pkgdir}/usr/libx32/lib${lib}.so
    echo "INPUT(-l${lib}w)" >${pkgdir}/usr/libx32/lib${lib}.so
    ln -sf lib${lib}w.a ${pkgdir}/usr/libx32/lib${lib}.a
  done
  ln -sf libncurses++w.a ${pkgdir}/usr/libx32/libncurses++.a

  # some packages look for -lcurses during build
  rm -f ${pkgdir}/usr/libx32/libcursesw.so
  echo "INPUT(-lncursesw)" >${pkgdir}/usr/libx32/libcursesw.so
  ln -sf libncurses.so ${pkgdir}/usr/libx32/libcurses.so
  ln -sf libncursesw.a ${pkgdir}/usr/libx32/libcursesw.a
  ln -sf libncurses.a ${pkgdir}/usr/libx32/libcurses.a

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}

# vim: set et ts=2 sw=2:
