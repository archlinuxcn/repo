# Maintainer:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Maintainer: Mateusz Gozdek <mgozdekof@gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>

pkgname=ncurses5-compat-libs
_pkgname=ncurses
pkgver=6.4
pkgrel=1
pkgdesc='System V Release 4.0 curses emulation library, ABI 5'
arch=(i686 x86_64)
url='http://invisible-island.net/ncurses/ncurses.html'
license=(MIT)
depends=(glibc gcc-libs sh)
provides=(libtinfo5)
conflicts=(libtinfo5)
source=(https://ftp.gnu.org/pub/gnu/ncurses/ncurses-$pkgver.tar.gz{,.sig})
sha256sums=('6931283d9ac87c5073f30b6290c4c75f21632bb4fc3603ac8100812bed248159'
            'SKIP')
validpgpkeys=('19882D92DDA4C400C22C0D56CC2AF4472167BE03')  # Thomas Dickey

build() {
  cd ${_pkgname}-${pkgver}

  ./configure \
    --prefix=/usr \
    --mandir=/usr/share/man \
    --with-shared \
    --with-normal \
    --without-debug \
    --without-ada \
    --enable-widec \
    --disable-pc-files \
    --with-cxx-binding \
    --with-cxx-shared \
    --with-versioned-syms \
    --with-abi-version=5
  make
}

package() {
  cd ${_pkgname}-${pkgver}
  make DESTDIR="$pkgdir" install.libs
  install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  rm -rf "$pkgdir/usr/include/" "$pkgdir/usr/lib/pkgconfig" \
    "$pkgdir"/usr/lib/*.so "$pkgdir"/usr/lib/*.a

  for lib in ncurses ncurses++ form panel menu; do
    ln -s /usr/lib/lib${lib}w.so.5 "$pkgdir/usr/lib/lib${lib}.so.5"
  done
  ln -s /usr/lib/libncurses.so.5 "$pkgdir/usr/lib/libtinfo.so.5"
  ln -s /usr/lib/libncurses.so.5 "$pkgdir/usr/lib/libtic.so.5"
}
