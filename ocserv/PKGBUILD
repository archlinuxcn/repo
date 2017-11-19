# Maintainer: Brian Bidulock <bidulock@openss7.org>
pkgname=ocserv
pkgver=0.11.9
pkgrel=1
pkgdesc="OpenConnect VPN Server"
arch=('i686' 'x86_64')
url="https://gitlab.com/ocserv/ocserv"
license=('GPL2')
depends=('autogen' 'libpcl' 'http-parser' 'libnl' 'libsystemd' 'protobuf-c' 'talloc' 'libseccomp' 'freeradius-client' 'libev' 'oath-toolkit' 'libwrap' 'geoip')
makedepends=('freeradius' 'gperf' 'tcp-wrappers')
backup=('etc/ocserv.config' 'etc/ocserv-passwd')
source=("$pkgname-$pkgver.tar.gz::https://gitlab.com/ocserv/ocserv/repository/archive.tar.gz?ref=ocserv_${pkgver//./_}")
sha256sums=('4f44d5351a8b329386693ba68527331d2f944f67c218dfce591e1eb2d1c2be7e')

prepare() {
  cd ${pkgname}-${pkgname}_*
  autoreconf -fi
}

build() {
  cd ${pkgname}-${pkgname}_*
  ./configure --prefix=/usr --sbindir=/usr/bin
  make
}

package() {
  cd ${pkgname}-${pkgname}_*
  make DESTDIR="$pkgdir" install
  install -Dm0644 doc/sample.config "$pkgdir/etc/ocserv.config"
  install -Dm0600 doc/sample.passwd "$pkgdir/etc/ocserv-passwd"
  install -Dm0644 doc/systemd/standalone/ocserv.service "$pkgdir/usr/lib/systemd/system/ocserv.service"
}
