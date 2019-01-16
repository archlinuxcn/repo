# Maintainer: Arthur Darcet <arthur.darcet at m4x.org>
# Contributor: Techlive Zheng <techlivezheng at gmail.com>

pkgname=libiconv
pkgver=1.15
pkgrel=1
pkgdesc='Provides libiconv.so and libcharset.so'
arch=('i686' 'x86_64')
url='http://www.gnu.org/software/libiconv/'
license=('LGPL')
source=("http://ftp.gnu.org/pub/gnu/${pkgname}/${pkgname}-${pkgver}.tar.gz")
md5sums=('ace8b5f2db42f7b3b3057585e80d9808')
options=(!libtool)

build() {
  cd $srcdir/${pkgname}-${pkgver}
  sed '/LD_RUN_PATH/d' -i Makefile.in
  ./configure --prefix=/usr
  cp -f /usr/include/stdio.h srclib/stdio.in.h
  make
}

package() {
  cd $srcdir/${pkgname}-${pkgver}
  make DESTDIR="$pkgdir" LIBDIR="/usr/lib" install
  mv "$pkgdir"/usr/include/{iconv.h,libiconv.h}
  mv "$pkgdir"/usr/bin/{iconv,libiconv}
  mv "$pkgdir"/usr/share/man/man1/{,lib}iconv.1
  mv "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv.3
  mv "$pkgdir"/usr/share/man/man3/{,libiconv_}iconvctl.3
  mv "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv_open.3
  mv "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv_close.3
  mv "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv_open_into.3
}
