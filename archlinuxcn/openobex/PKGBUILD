# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributor: Geoffroy Carrier <geoffroy@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: damir <damir@archlinux.org>

pkgname=openobex
pkgver=1.7.2
pkgrel=3
pkgdesc="Implementation of the OBject EXchange (OBEX) protocol"
url="http://dev.zuckschwerdt.org/openobex/"
arch=('x86_64' 'i686')
license=('GPL' 'LGPL')
depends=('libusbx' 'bluez-libs')
makedepends=('cmake' 'libxslt' 'doxygen' 'java-environment')
options=('staticlibs' '!makeflags')
source=(http://downloads.sourceforge.net/${pkgname}/${pkgname}-${pkgver}-Source.tar.gz)
md5sums=('f6e0b6cb7dcfd731460a7e9a91429a3a')

prepare() {
  sed -i 's|MODE="660", GROUP="plugdev"|TAG+="uaccess"|' ${pkgname}-${pkgver}-Source/udev/openobex.rules.in
}

build() {
  mkdir build
  cd build
  cmake ../${pkgname}-${pkgver}-Source \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_RPATH=ON \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DCMAKE_INSTALL_SBINDIR=/usr/bin \
    -DCMAKE_INSTALL_UDEVRULESDIR=/usr/lib/udev/rules.d
  make all openobex-apps
}

package() {
  cd build
  make DESTDIR="${pkgdir}" install
  cp ../${pkgname}-${pkgver}-Source/apps/lib/*.h  "${pkgdir}/usr/include/openobex/"
  install -m644 apps/lib/libopenobex-apps-common.a "${pkgdir}/usr/lib/libopenobex-apps-common.a"
}
