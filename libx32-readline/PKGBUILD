# $Id: PKGBUILD 140619 2015-09-17 21:06:07Z foutrelis $
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=readline
pkgname=libx32-$_pkgbasename
_basever=6.3
_patchlevel=008 #prepare for some patches
pkgver=$_basever.$_patchlevel
pkgrel=2.1
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
validpgpkeys=('7C0135FB088AAF6C66C650B9BB5869F064EA74AB') # Chet Ramey

md5sums=('33c8fb279e981274f485fd91da77e94a'
         '4343f5ea9b0f42447f102fb61576b398'
         'SKIP'
         '700295212f7e2978577feaee584afddb'
         'SKIP'
         'af4963862f5156fbf9111c2c6fa86ed7'
         'SKIP'
         '11f9def89803a5052db3ba72394ce14f'
         'SKIP'
         '93721c31cd225393f80cb3aadb165544'
         'SKIP'
         '71dc6ecce66d1489b96595f55d142a52'
         'SKIP'
         '062a08ed60679d3c4878710b3d595b65'
         'SKIP'
         'ee1c04072154826870848d8b218d7b04'
         'SKIP')

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
