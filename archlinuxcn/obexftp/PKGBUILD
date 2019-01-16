# Maintainer: xiretza <xiretza+aur@gmail.com>
# Contributor: Giovanni Scafora <giovanni@archlinux.org>
# Contributor: Alessio 'mOLOk' Bolognino <themolok@gmail.com>

pkgname=obexftp
pkgver=0.24.2
pkgrel=4
pkgdesc="A tool for transfer files to/from any OBEX enabled device"
arch=('x86_64')
url="http://dev.zuckschwerdt.org/openobex/wiki/ObexFtp"
license=('GPL')
provides=("obexfs=${pkgver}")
replaces=('obexfs')
conflicts=('obexfs')
depends=('openobex' 'expat' 'fuse2')
makedepends=('cmake' 'asciidoc' 'xmlto' 'swig' 'ruby' 'tk')
optdepends=('ruby: ruby bindings'
            'tk: TCL/Tk bindings')
options=('!makeflags' '!docs')
source=("http://downloads.sourceforge.net/openobex/${pkgname}-${pkgver}-Source.tar.gz"
        "explicitly-link-libbfb-and-libmulticobex.patch")
sha256sums=('d40fb48e0a0eea997b3e582774b29f793919a625d54b87182e31a3f3d1c989a3'
            'b2bdc9c9ad1894864d77531549be6f921f8d04344c64185ca053cc677c609a50')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}-Source"
  patch -p1 < "${srcdir}/explicitly-link-libbfb-and-libmulticobex.patch"
}

build() {
  cd "${srcdir}/"

  mkdir build
  cd build
  cmake "../${pkgname}-${pkgver}-Source" \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_RPATH=ON \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_INSTALL_SBINDIR=bin \
    -DENABLE_PERL=YES \
    -DENABLE_PYTHON=YES \
    -DENABLE_RUBY=YES \
    -DENABLE_TCL=YES
  make doc
}

package() {
  cd "${srcdir}/build"

  make DESTDIR="${pkgdir}" install
}
