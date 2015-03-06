# $Id: PKGBUILD 226133 2014-11-12 19:06:51Z eric $
# Maintainer: Eric Bélanger <eric@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=binx32-tk
pkgver=8.6.3
pkgrel=1.1
pkgdesc="A windowing toolkit for use with tcl (x32 ABI)"
arch=('x86_64')
url="http://tcl.sourceforge.net/"
license=('custom')
depends=("tk" "binx32-tcl=${pkgver}" 'libx32-libxss' 'libx32-libxft')
makedepends=("gcc-multilib-x32")
options=('staticlibs')
source=(http://downloads.sourceforge.net/sourceforge/tcl/tk${pkgver}-src.tar.gz)
sha1sums=('244ddc0f64cc3d429c9d86135d0bbe2cf06c9360')

build() {
  cd tk${pkgver}/unix

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./configure --prefix=/usr --mandir=/usr/share/man --enable-threads --libdir=/usr/libx32 --disable-rpath

  # http://cblfs.cross-lfs.org/index.php/Tk
  sed -i 's@/lib/@/libx32/@' Makefile

  make
}

check() {
  cd tk${pkgver}/unix
#  make test
}

package() {
  cd tk${pkgver}/unix
  make INSTALL_ROOT="${pkgdir}" install install-private-headers
  mv ${pkgdir}/usr/bin/wish${pkgver%.*} ${pkgdir}/usr/bin/wish${pkgver%.*}-x32
  ln -sf wish${pkgver%.*}-x32 "${pkgdir}/usr/bin/wish-x32"
  ln -sf libtk${pkgver%.*}.so "${pkgdir}/usr/libx32/libtk.so"

  # remove duplicate include and manual files
  rm -rf ${pkgdir}/usr/{include,share}

  install -Dm644 license.terms "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # remove buildroot traces
  sed -e "s#${srcdir}/tk${pkgver}/unix#/usr/libx32#" \
      -e "s#${srcdir}/tk${pkgver}#/usr/include#" \
      -i "${pkgdir}/usr/libx32/tkConfig.sh"
}
