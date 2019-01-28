# Maintainer: Brian Bidulock <bidulock@openss7.org>
pkgname=ocserv
pkgver=0.12.2
pkgrel=1
pkgdesc="OpenConnect VPN Server"
arch=('i686' 'x86_64')
url="https://gitlab.com/ocserv/ocserv"
license=('GPL2')
depends=('autogen' 'libpcl' 'http-parser' 'libnl' 'libsystemd' 'protobuf-c' 'talloc' 'libseccomp' 'freeradius-client' 'libev' 'oath-toolkit' 'libwrap' 'geoip')
makedepends=('freeradius' 'gperf' 'tcp-wrappers')
backup=('etc/ocserv.config' 'etc/ocserv-passwd')
source=("$pkgname-$pkgver.tar.gz::https://gitlab.com/ocserv/ocserv/repository/archive.tar.gz?ref=ocserv_${pkgver//./_}")
sha256sums=('3ebcad5855691c302d46957c035f3c01d0c8e2d275cfca78abbb37fdaf91c204')

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
sha256sums=('da318005266de07d257daf407d087446d993c9035d4ca00156f65c3bae1ec851')
