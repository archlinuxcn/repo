# $Id: PKGBUILD 96305 2013-08-24 19:57:20Z bluewind $
# Upstream Maintainer: Allan McRae <allan@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>
# Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=ncurses
pkgname=libx32-${_pkgbasename}
pkgver=5.9
pkgrel=2
pkgdesc="System V Release 4.0 curses emulation library (x32 ABI)"
arch=('x86_64')
url="http://www.gnu.org/software/ncurses/"
license=('MIT')
depends=('libx32-glibc' ${_pkgbasename})
makedepends=("gcc-multilib-x32")
source=(ftp://ftp.gnu.org/pub/gnu/${_pkgbasename}/${_pkgbasename}-${pkgver}.tar.gz)
md5sums=('8cb9c412e5f2d96bc6f459aa8c6282a1')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd ${srcdir}/
  mkdir ncurses{,w}-build

  cd ${srcdir}/ncursesw-build
  ../${_pkgbasename}-${pkgver}/configure --prefix=/usr --mandir=/usr/share/man \
     --with-shared --with-normal --without-debug --without-ada --without-gpm \
     --with-install-prefix=${pkgdir} --enable-widec --libdir=/usr/libx32
  make

  # libraries for external binary support
  cd ${srcdir}/ncurses-build
#  [ $CARCH = "x86_64" ] && CONFIGFLAG="--with-chtype=long"
  ../${_pkgbasename}-${pkgver}/configure --prefix=/usr \
    --with-shared --with-normal --without-debug --without-ada --without-gpm \
    --with-install-prefix=${pkgdir} $CONFIGFLAG --libdir=/usr/libx32
  make
}

package() {
  cd ${srcdir}/ncursesw-build
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

  # non-widec compatibility libraries
  cd ${srcdir}/ncurses-build
  for lib in ncurses form panel menu; do
    install -Dm755 lib/lib${lib}.so.${pkgver} ${pkgdir}/usr/libx32/lib${lib}.so.${pkgver}
    ln -s lib${lib}.so.${pkgver} ${pkgdir}/usr/libx32/lib${lib}.so.5
  done

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}

# vim: set et ts=2 sw=2:
