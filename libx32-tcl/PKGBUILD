# $Id$
# Maintainer: Miguel Revilla <yo@miguelrevilla.com>
# Contributor: Eric Bélanger <eric@archlinux.org>

_pkgbasename=tcl
pkgname=libx32-${_pkgbasename}
pkgver=8.6.4
pkgrel=1.1
pkgdesc="The Tcl scripting language (x32 ABI runtime)"
arch=('x86_64')
url="http://tcl.sourceforge.net/"
license=('custom')
depends=('tcl' 'libx32-zlib')
source=(http://downloads.sourceforge.net/sourceforge/tcl/tcl${pkgver}-src.tar.gz)
md5sums=('d7cbb91f1ded1919370a30edd1534304')

prepare() {
  cd tcl${pkgver}
  # we build the tcl sqlite interface in sqlite-tcl package
  rm -rf pkgs/sqlite3*

  sed -i 's/#define DUPTRAVERSE_MAX_DEPTH 500/#define DUPTRAVERSE_MAX_DEPTH 5000/' \
    generic/regc_nfa.c
}

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd tcl${pkgver}/unix
  ./configure --prefix=/usr --libdir=/usr/libx32 --mandir=/usr/share/man --enable-threads
  make
}

check() {
  cd tcl${pkgver}/unix
  make test
}

package() {
  cd tcl${pkgver}/unix
  make INSTALL_ROOT="${pkgdir}" install install-private-headers
  find "${pkgdir}" -name '*.a' -type f -exec chmod 644 {} \;
  ln -sf tclsh8.6 "${pkgdir}/usr/bin/tclsh"

  # remove 64-bit and unarched stuff
  rm -rf "${pkgdir}"/usr/{include,share,bin,lib}
  mkdir -p "${pkgdir}/usr/share/licenses"
  ln -s $_pkgbasename "${pkgdir}/usr/share/licenses/${pkgname}"

  # remove buildroot traces
  sed -i "s#${srcdir}#/usr/src#" "${pkgdir}"/usr/libx32/{tcl,tdbc1.0.3/tdbc,itcl4.0.3/itcl}Config.sh
}
