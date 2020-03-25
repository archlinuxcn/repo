# Maintainer: Brian Bidulock <bidulock@openss7.org>
pkgname=ocserv
pkgver=1.0.0
pkgrel=1
pkgdesc="OpenConnect VPN Server"
arch=('i686' 'x86_64')
url="https://gitlab.com/ocserv/ocserv"
license=('GPL2')
depends=('autogen' 'libpcl' 'http-parser' 'libnl' 'libsystemd' 'protobuf-c' 'talloc' 'libseccomp' 'freeradius-client' 'libev' 'oath-toolkit' 'libwrap' 'geoip')
makedepends=('freeradius' 'gperf' 'tcp-wrappers')
backup=('etc/ocserv.config' 'etc/ocserv-passwd')
source=("$pkgname-$pkgver.tar.gz::https://gitlab.com/ocserv/ocserv/repository/archive.tar.gz?ref=${pkgver}")
sha256sums=('52a9c9234bc009143622d5cd28ed15984afa26200bae74d60a8c0ad483a7de58')

prepare() {
  cd ${pkgname}-${pkgver}-*
  autoreconf -fi
}

build() {
  cd ${pkgname}-${pkgver}-*
  ./configure --prefix=/usr --sbindir=/usr/bin
  make
}

package() {
  cd ${pkgname}-${pkgver}-*
  make DESTDIR="$pkgdir" install
  install -Dm0644 doc/sample.config "$pkgdir/etc/ocserv.config"
  install -Dm0600 doc/sample.passwd "$pkgdir/etc/ocserv-passwd"
  install -Dm0644 doc/systemd/standalone/ocserv.service "$pkgdir/usr/lib/systemd/system/ocserv.service"
}
