# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: David Runge <dave@sleepmap.de>
# Contributor: speps <speps at aur dot archlinux dot org>
# Contributor: Ray Rashif <schiv@archlinux.org>
# Contributor: Wieland Hoffmann <the_mineo@web.de>
# Contributor: Birger Moellering <bmoellering@googlemail.com>
# 2018/01/03: <dropped from community; upstream dead, unneeded>
# 2012/06/05: <added into community as supercollider dependency>
# 2012/03/21: <dropped from community; broken + see bug #28344>

pkgname=cwiid
pkgver=svn_history
pkgrel=3
pkgdesc="Linux Nintendo Wiimote interface"
arch=("x86_64")
url="https://github.com/abstrakraft/${pkgname}"
depends=("bluez-libs" "gtk2" "python2")
license=("GPL2")
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/abstrakraft/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('31d3e843c107f07e2b425bee17dafa215937c582b3b4d9c7bc71f4edcfe5ea68')

#cwiid-0.6.00 trunk@201 918edb2d-ff29-0410-9de2-eb38e7f22bc7
#svn_history-0-g3163ded

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  msg2 "Fixing ldconfig use in configure"
  sed -i "/ldconfig/s/WITH/ENABLE/" "${srcdir}/${pkgname}-${pkgver}/configure.ac"
  autoreconf -fi
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --with-python=python2 \
    --enable-ldconfig=no
  LDFLAGS+=" -pthread -lpthread -lbluetooth" make
}

package() {
  msg2 "Installing application"
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  msg2 "Installing wminput README"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/wminput/README" "${pkgdir}/usr/share/doc/${pkgname}/wminput/README"
}
