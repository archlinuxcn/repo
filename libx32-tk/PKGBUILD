# $Id: PKGBUILD 220811 2014-08-30 02:45:43Z eric $
# Maintainer: Eric Bélanger <eric@archlinux.org>

pkgname=libx32-tk
pkgver=8.6.4
pkgrel=1.1
pkgdesc="A windowing toolkit for use with tcl"
arch=('x86_64')
url="http://tcl.sourceforge.net/"
license=('custom')
depends=("libx32-tcl=${pkgver}" 'libx32-libxss' 'libx32-libxft' 'tk')
options=('staticlibs')
source=(http://downloads.sourceforge.net/sourceforge/tcl/tk${pkgver}-src.tar.gz)
sha1sums=('ad24c59ac2e7453d1ed2bad0d7d18a01eabc5226')

build() {
  cd tk${pkgver}/unix
  export CC='gcc -mx32'
  export CXX='g++ -mx32'
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"
  export LDFLAGS+='-L/usr/libx32'
  ./configure --prefix=/usr --mandir=/usr/share/man \
    --enable-threads --disable-rpath \
    --libdir=/usr/libx32 \
    --libexecdir=/usr/libx32 \
    --with-tcl=/usr/libx32/
  make
}

check() {
  cd tk${pkgver}/unix
  # make test
}

package() {
  cd tk${pkgver}/unix
  make INSTALL_ROOT="${pkgdir}" install install-private-headers
  mv "${pkgdir}/usr/bin/wish${pkgver%.*}" \
    "${pkgdir}/usr/bin/wish${pkgver%.*}-x32"
  ln -sf wish${pkgver%.*}-x32 "${pkgdir}/usr/bin/wish-x32"
  ln -sf libtk${pkgver%.*}.so "${pkgdir}/usr/libx32/libtk.so"

  rm -rf "${pkgdir}/usr/"{share/man,include,lib}

  install -Dm644 license.terms "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # remove buildroot traces
  sed -e "s#${srcdir}/tk${pkgver}/unix#/usr/libx32#" \
      -e "s#${srcdir}/tk${pkgver}#/usr/include#" \
      -i "${pkgdir}/usr/libx32/tkConfig.sh"
}
