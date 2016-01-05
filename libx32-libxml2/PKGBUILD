# $Id: PKGBUILD 153369 2015-12-15 09:52:04Z fyan $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# Contributor: John Proctor <jproctor@prium.net>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libxml2
pkgname=libx32-$_pkgbasename
pkgver=2.9.3
pkgrel=1.1
pkgdesc="XML parsing library, version 2 (x32 ABI)"
arch=(x86_64)
license=('custom')
depends=('libx32-zlib>=1.2.4' 'libx32-readline>=6.1' 'libx32-ncurses>=5.7' $_pkgbasename)
makedepends=(gcc-multilib-x32)
options=('!libtool')
url="http://www.xmlsoft.org/"
source=(ftp://ftp.xmlsoft.org/${_pkgbasename}/${_pkgbasename}-${pkgver}.tar.gz)
md5sums=('daece17e045f1c107610e137ab50c179')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  autoreconf -fi
  ./configure --prefix=/usr --with-threads --with-history --libdir=/usr/libx32 --without-lzma
  
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

  make
}

package() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share,bin} "$pkgdir/usr/libx32/xml2Conf.sh"
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
