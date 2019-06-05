# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Contributor: Arthur Darcet <arthur.darcet at m4x.org>
# Contributor: Techlive Zheng <techlivezheng at gmail.com>

pkgname=libiconv
pkgver=1.16
pkgrel=1
pkgdesc='Provides libiconv.so and libcharset.so'
arch=('i686' 'x86_64')
url='http://www.gnu.org/software/libiconv/'
license=('LGPL')
source=("http://ftp.gnu.org/pub/gnu/${pkgname}/${pkgname}-${pkgver}.tar.gz"{,.sig})
sha512sums=('365dac0b34b4255a0066e8033a8b3db4bdb94b9b57a9dca17ebf2d779139fe935caf51a465d17fd8ae229ec4b926f3f7025264f37243432075e5583925bb77b7'
            'SKIP')
options=(!libtool)
validpgpkeys=(
  '68D94D8AAEEAD48AE7DC5B904F494A942E4616C2' # Bruno Haible
)

build() {
  cd "${pkgname}-${pkgver}"
  sed '/LD_RUN_PATH/d' -i Makefile.in
  ./configure --prefix=/usr
  cp -f /usr/include/stdio.h srclib/stdio.in.h
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" LIBDIR="/usr/lib" install
  mv "$pkgdir"/usr/include/{iconv.h,libiconv.h}
  mv "$pkgdir"/usr/bin/{iconv,libiconv}
  mv "$pkgdir"/usr/share/man/man1/{,lib}iconv.1
  mv "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv.3
  mv "$pkgdir"/usr/share/man/man3/{,libiconv_}iconvctl.3
  mv "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv_open.3
  mv "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv_close.3
  mv "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv_open_into.3
}
