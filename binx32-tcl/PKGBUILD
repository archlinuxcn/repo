# $Id: PKGBUILD 226131 2014-11-12 18:46:40Z eric $
# Maintainer: Eric Bélanger <eric@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=binx32-tcl
pkgver=8.6.3
pkgrel=1.2
pkgdesc="The Tcl scripting language (x32 ABI)"
arch=('x86_64')
url="http://tcl.sourceforge.net/"
license=('custom')
depends=('libx32-zlib' 'tcl')
makedepends=("gcc-multilib-x32")
options=('staticlibs')
source=(http://downloads.sourceforge.net/sourceforge/tcl/tcl${pkgver}-src.tar.gz)
sha1sums=('026b4b6330205bdc49af12332ee17c2b01f76d37')

prepare() {
  cd tcl${pkgver}
  # we build the tcl sqlite interface in sqlite-tcl package
  rm -rf pkgs/sqlite3*
}

build() {
  cd tcl${pkgver}/unix
  
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  # http://cblfs.cross-lfs.org/index.php/TCL
  sed -i '/sprintf(installLib/s:"lib:&x32:' tclUnixInit.c
  sed -i -e '/TCL_PACKAGE_PATH=/s:=.*:="/usr/libx32":' \
         -e "/^TCL_LIBRARY=/s:=.*:='/usr/libx32/tcl\$(VERSION)':" configure

  ./configure --prefix=/usr --mandir=/usr/share/man --libdir=/usr/libx32 --enable-threads
  make
}

check() {
  cd tcl${pkgver}/unix
  make test
}

package() {
  cd tcl${pkgver}/unix
  make INSTALL_ROOT="${pkgdir}" install install-private-headers
  mv ${pkgdir}/usr/bin/tclsh${pkgver%.*} ${pkgdir}/usr/bin/tclsh${pkgver%.*}-x32
  ln -sf tclsh${pkgver%.*}-x32 "${pkgdir}/usr/bin/tclsh-x32"
  ln -sf libtcl${pkgver%.*}.so "${pkgdir}/usr/libx32/libtcl.so"

  # remove duplicate include and manual files
  rm -rf ${pkgdir}/usr/{share,include}

  install -Dm644 ../license.terms "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # remove buildroot traces
  sed -e "s#${srcdir}/tcl${pkgver}/unix#/usr/libx32#" \
      -e "s#${srcdir}/tcl${pkgver}#/usr/include#" \
      -i "${pkgdir}/usr/libx32/tclConfig.sh"

  tdbcver=tdbc1.0.2
  sed -e "s#${srcdir}/tcl${pkgver}/unix/pkgs/$tdbcver#/usr/libx32/$tdbcver#" \
      -e "s#${srcdir}/tcl${pkgver}/pkgs/$tdbcver/generic#/usr/include#" \
      -e "s#${srcdir}/tcl${pkgver}/pkgs/$tdbcver/library#/usr/libx32/tcl${pkgver%.*}#" \
      -e "s#${srcdir}/tcl${pkgver}/pkgs/$tdbcver#/usr/include#" \
      -i "${pkgdir}/usr/libx32/$tdbcver/tdbcConfig.sh"

  itclver=itcl4.0.2
  sed -e "s#${srcdir}/tcl${pkgver}/unix/pkgs/$itclver#/usr/libx32/$itclver#" \
      -e "s#${srcdir}/tcl${pkgver}/pkgs/$itclver/generic#/usr/include#" \
      -e "s#${srcdir}/tcl${pkgver}/pkgs/$itclver#/usr/include#" \
      -i "${pkgdir}/usr/libx32/$itclver/itclConfig.sh"
}
