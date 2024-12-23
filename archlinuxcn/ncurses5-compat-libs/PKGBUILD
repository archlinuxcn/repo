# Contributor:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Mateusz Gozdek <mgozdekof@gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>

pkgname=ncurses5-compat-libs
_pkgname=ncurses
pkgver=6.5
pkgrel=1
pkgdesc='System V Release 4.0 curses emulation library, ABI 5'
arch=(i686 x86_64)
url='http://invisible-island.net/ncurses/ncurses.html'
license=(MIT)
depends=(glibc gcc-libs sh)
provides=(libtinfo5)
conflicts=(libtinfo5)
source=(https://ftp.gnu.org/pub/gnu/ncurses/ncurses-$pkgver.tar.gz{,.sig})
sha256sums=('136d91bc269a9a5785e5f9e980bc76ab57428f604ce3e5a5a90cebc767971cc6'
            'SKIP')
validpgpkeys=('19882D92DDA4C400C22C0D56CC2AF4472167BE03')  # Thomas Dickey

prepare() {
  cp -r ${_pkgname}-${pkgver}{,-no-widec}
}

build() {
  local configure_options=(
    --prefix=/usr
    --mandir=/usr/share/man
    --with-shared
    --with-normal
    --without-debug
    --without-ada
    --disable-pc-files
    --with-cxx-binding
    --with-cxx-shared
    --with-versioned-syms
    --with-abi-version=5
  )

  cd "${srcdir}/${_pkgname}-${pkgver}"

  ./configure "${configure_options[@]}" --enable-widec
  make

  cd "${srcdir}/${_pkgname}-${pkgver}-no-widec"

  ./configure "${configure_options[@]}"
  make
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  make DESTDIR="$pkgdir" install.libs
  cd "${srcdir}/${_pkgname}-${pkgver}-no-widec"
  make DESTDIR="$pkgdir" install.libs
  install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  rm -rf "$pkgdir/usr/include/" "$pkgdir/usr/lib/pkgconfig" \
    "$pkgdir"/usr/lib/*.so "$pkgdir"/usr/lib/*.a

  ln -s /usr/lib/libncurses.so.5 "$pkgdir/usr/lib/libtinfo.so.5"
  ln -s /usr/lib/libncurses.so.5 "$pkgdir/usr/lib/libtic.so.5"
}
