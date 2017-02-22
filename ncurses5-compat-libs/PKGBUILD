# Maintainer:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>

pkgname=ncurses5-compat-libs
_pkgname=ncurses
_pkgver=6.0-20161224
pkgver=${_pkgver/-/+}
pkgrel=1
pkgdesc='System V Release 4.0 curses emulation library, ABI 5'
arch=('i686' 'x86_64')
url='http://invisible-island.net/ncurses/ncurses.html'
license=('MIT')
depends=('glibc' 'gcc-libs' 'sh')
provides=('libtinfo5')
conflicts=('libtinfo5')
source=(http://invisible-mirror.net/archives/ncurses/current/ncurses-${_pkgver}.tgz{,.asc})
md5sums=('18d398f6120e6734b7a237f4bd3b9d21'
         'SKIP')
validpgpkeys=('C52048C0C0748FEE227D47A2702353E0F7E48EDB')  # Thomas Dickey

build() {
  cd ${_pkgname}-${_pkgver}

  ./configure --prefix=/usr --mandir=/usr/share/man \
    --with-shared --with-normal --without-debug --without-ada --enable-widec \
    --disable-pc-files --with-cxx-binding --with-cxx-shared --with-abi-version=5
  make
}

package() {
  cd ${_pkgname}-${_pkgver}
  make DESTDIR="$pkgdir" install.libs
  rm -rf "$pkgdir"/usr/include/ "$pkgdir"/usr/lib/pkgconfig \
    "$pkgdir"/usr/lib/*.so

  # fool packages looking to link to non-wide-character ncurses libraries
  for lib in ncurses ncurses++ form panel menu; do
    ln -s /usr/lib/lib${lib}w.so.5 "$pkgdir/usr/lib/lib${lib}.so.5"
  done
  ln -s /usr/lib/libncurses.so.5 "$pkgdir/usr/lib/libtinfo.so.5"

  # install license, rip it from the readme
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  grep -B 100 '$Id' README > "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

}
