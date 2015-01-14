# Maintainer: zml <zach at zachsthings dot com>
# Contributor: Ambroz Bizjak <ambrop7 at gmail dot com>

pkgname=badvpn
pkgver=1.999.129
pkgrel=1
pkgdesc="Peer-to-peer VPN system, and NCD, a programming language for network interface configuration"
arch=('i686' 'x86_64')
url="https://github.com/ambrop72/badvpn"
license=('GPL')
depends=('nss' 'openssl' 'iproute2')
makedepends=('cmake')
source=("https://github.com/ambrop72/badvpn/archive/${pkgver}.tar.gz"
	'badvpn-ncd.service'
	'badvpn-ncd.conf.d')
md5sums=('e42f9c22fcef5a44498e80f23ceee0b3'
         '35cf690b7cdf90fdb7abf9edcd5e4540'
         '19ea2de11e1623c5e91a363e72c329f1')

build() {
	cd ${srcdir}/${pkgname}-${pkgver} || return 1
	cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release . || return 1
	make || return 1
}

package() {
	cd ${srcdir}/${pkgname}-${pkgver} || return 1
	make DESTDIR=${pkgdir} install || return 1

	install -D -m755 "$srcdir/badvpn-ncd.service" "$pkgdir/usr/lib/systemd/system/badvpn-ncd.service" || return 1
	install -D -m0644 "$srcdir/badvpn-ncd.conf.d" "$pkgdir/etc/conf.d/badvpn-ncd" || return 1
}
