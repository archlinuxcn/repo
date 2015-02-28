# $Id: PKGBUILD 112797 2014-06-07 12:10:12Z bluewind $
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>
# Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=readline
pkgname=libx32-$_pkgbasename
_basever=6.3
_patchlevel=000 #prepare for some patches
pkgver=6.3.006
pkgrel=1.1
pkgdesc="GNU readline library (x32 ABI)"
arch=(x86_64)
url="http://tiswww.case.edu/php/chet/readline/rltop.html"
license=('GPL')
depends=('libx32-glibc' 'libx32-ncurses' $_pkgbasename)
makedepends=('gcc-multilib-x32')
source=(http://ftp.gnu.org/gnu/readline/readline-$_basever.tar.gz)
if [ $_patchlevel -gt 00 ]; then
    for (( p=1; p<=$((10#${_patchlevel})); p++ )); do
      source=(${source[@]} http://ftp.gnu.org/gnu/readline/readline-$_basever-patches/readline${_basever//./}-$(printf "%03d" $p){,.sig})
    done
fi
md5sums=('33c8fb279e981274f485fd91da77e94a')

build() {
  cd ${srcdir}/${_pkgbasename}-$_basever

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  for (( p=1; p<=$((10#${_patchlevel})); p++ )); do
    msg "applying patch readline${_basever//./}-$(printf "%03d" $p)"
    patch -Np0 -i $srcdir/readline${_basever//./}-$(printf "%03d" $p)
  done

  # Remove RPATH from shared objects (FS#14366)
  sed -i 's|-Wl,-rpath,$(libdir) ||g' support/shobj-conf

  ./configure --prefix=/usr --libdir=/usr/libx32
  make SHLIB_LIBS=-lncurses
}

package() {
  cd ${srcdir}/${_pkgbasename}-$_basever

  make DESTDIR=${pkgdir} install
  rm -rf "${pkgdir}"/usr/{include,share,bin}
}
